# Game Routes

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A game has $n$ levels, connected by $m$ teleporters, and your task is to get from level $1$ to level $n$. The game has been designed so that there are no directed cycles in the underlying graph. In how many ways can you complete the game?


## Input


The first input line has two integers $n$ and $m$: the number of levels and teleporters. The levels are numbered $1,2,\dots,n$.


After this, there are $m$ lines describing the teleporters. Each line has two integers $a$ and $b$: there is a teleporter from level $a$ to level $b$.


## Output


Print one integer: the number of ways you can complete the game. Since the result may be large, print it modulo $10^9+7$.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
4 5
1 2
2 4
1 3
3 4
1 4
```


Output:


```
3
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
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, m; cin>>n>>m;
  grid edg(n+1); fir(m){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
  }

  vi dp(n+1, -1);
  function<void(ll)> rec=[&](ll at){
    if(dp[at]+1) return;
    if(at==n) {dp[n]=1; return;}

    dp[at]=0;
    for(ll to: edg[at]){
      rec(to);
      dp[at]=(dp[at]+dp[to])%mod; 
    }
  }; rec(1);

  cout<<dp[1]<<en;
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
