# Distinct Colors

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a rooted tree consisting of $n$ nodes. The nodes are numbered $1,2,\ldots,n$, and node $1$ is the root. Each node has a color.


Your task is to determine for each node the number of distinct colors in the subtree of the node.


## Input


The first input line contains an integer $n$: the number of nodes. The nodes are numbered $1,2,\ldots,n$.


The next line consists of $n$ integers $c_1,c_2,\ldots,c_n$: the color of each node.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


## Output


Print $n$ integers: for each node $1,2,\ldots,n$, the number of distinct colors.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a,b \le n$
- $1 \le c_i \le 10^9$


## Example


Input:


```
5
2 3 2 2 1
1 2
1 3
3 4
3 5
```


Output:


```
3 1 2 1 1
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
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)

ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

void solve(){
  ll n; cin>>n;
  vi v(n+1); fir(n) cin>>v[i+1];
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }

  ll tm=0;
  vi ss(n+1), st(n+1), et(n);
  function<void(ll, ll)> dfs=[&](ll at, ll pr){
    ss[at]=1; et[tm]=at; st[at]=tm;
    tm++;
    for(ll to: edg[at]) if(to-pr){
      dfs(to, at);
      ss[at]+=ss[to];
    }
  }; dfs(1, 0);

  unordered_set<ll> col; 
  vi res(n+1);
  function<void(ll, ll, bool)> hld=[&](ll at, ll pr, ll kp){
    ll bc=-1, bi=-1;
    for(ll to: edg[at]) if(to-pr and ss[to]>bc) bc=ss[to], bi=to; 

    for(ll to: edg[at]) if(to-pr and to-bi) hld(to, at, 0);
    if(bi+1) hld(bi, at, 1);

    col.insert(v[at]);
    for(ll to: edg[at]) if(to-pr and to-bi){
      fir(ss[to]) col.insert(v[et[st[to]+i]]);
    }
    res[at]=sz(col);

    if(!kp){
      fir(ss[at]) col.erase(v[et[st[at]+i]]);
    }
  }; hld(1, 0, 1);

  fir(n) cout<<res[i+1]<<ln;
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
