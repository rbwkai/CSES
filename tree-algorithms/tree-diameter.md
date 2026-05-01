# Tree Diameter

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a tree consisting of $n$ nodes.


The diameter of a tree is the maximum distance between two nodes. Your task is to determine the diameter of the tree.


## Input


The first input line contains an integer $n$: the number of nodes. The nodes are numbered $1,2,\ldots,n$.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


## Output


Print one integer: the diameter of the tree.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5
1 2
1 3
3 4
3 5
```


Output:


```
3
```


Explanation: The diameter corresponds to the path $2 \rightarrow 1 \rightarrow 3 \rightarrow 5$.



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
  ll n; cin>>n;
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }

  grid dp(n+1, vi(2));
  function<void(ll, ll)> rec=[&](ll nd, ll pr){
    for(ll to: edg[nd]) if(to!=pr){
      rec(to, nd);
    }
    
    ll gv=-1, mg=0;
    ll da=0;
    for(ll to: edg[nd]) if(to!=pr){
      if(dp[to][0]>gv) gv=dp[to][0], mg=to;
      da=max(da, dp[to][1]);
    }

    da=max(da, gv+1);
    for(ll to: edg[nd]) if(to!=pr and to!=mg) da=max(da, 2+gv+dp[to][0]);

    dp[nd][0]=1+gv;
    dp[nd][1]=da;
  };

  rec(1, 0);
  cout<<dp[1][1]<<en;
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
