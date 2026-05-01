# Counting Paths

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a tree consisting of $n$ nodes, and $m$ paths in the tree.


Your task is to calculate for each node the number of paths containing that node.


## Input


The first input line contains integers $n$ and $m$: the number of nodes and paths. The nodes are numbered $1,2,\ldots,n$.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


Finally, there are $m$ lines describing the paths. Each line contains two integers $a$ and $b$: there is a path between nodes $a$ and $b$.


## Output


Print $n$ integers: for each node $1,2,\ldots,n$, the number of paths containing that node.


## Constraints


- $1 \le n, m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 3
1 2
1 3
3 4
3 5
1 3
2 5
1 4
```


Output:


```
3 1 3 1 1
```


---

## Solution

```cpp
//#pragma GCC optimize("Ofast,unroll-loops")
//#pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma,tune=native")
 
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
 
using namespace std;
using namespace __gnu_pbds;
using ll = long long;
using vi = vector<ll>;
using pi = pair<ll, ll>;
using grid = vector<vi>;
 
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;

void solve(){
  ll n, q; cin>>n>>q;
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }

  grid bin(n+1, vi(20));
  vi dp(n+1);
  function<void(ll, ll)> rec=[&](ll c, ll p){
    for(auto t: edg[c]) if(t-p){
      dp[t]=dp[c]+1;
      bin[t][0]=c;
      rec(t, c);
    }
  }; rec(1, 0);

  fjr(20) fir(n) if(j) bin[i+1][j]=bin[ bin[i+1][j-1] ][j-1];
  
  function<ll(ll, ll)> lca=[&](ll a, ll b){
    if(dp[a]>dp[b]) swap(a, b);

    ll jr=dp[b]-dp[a];
    fir(20) if((jr>>i)&1) b=bin[b][i];

    if(a==b){
      return a;
    }
    fir(20){
      ll ch=19-i;
      if(bin[a][ch]!=bin[b][ch]) a=bin[a][ch], b=bin[b][ch];
    }
    return bin[a][0];
  };

  vi df(n+1);
  while(q--){
    ll a, b; cin>>a>>b;
    df[a]++; df[b]++;
    df[lca(a, b)]--; df[bin[lca(a, b)][0]]--;
  }

  function<void(ll, ll)> dfs=[&](ll c, ll p){
    for(ll to: edg[c]) if(to-p){
      dfs(to, c);
      df[c]+=df[to];
    }
  }; dfs(1, 0);

  fir(n) cout<<df[i+1]<<ln;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
