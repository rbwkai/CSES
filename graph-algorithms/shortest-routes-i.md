# Shortest Routes I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ cities and $m$ flight connections between them. Your task is to determine the length of the shortest route from Syrjälä to every city.


## Input


The first input line has two integers $n$ and $m$: the number of cities and flight connections. The cities are numbered $1,2,\dots,n$, and city $1$ is Syrjälä.


After that, there are $m$ lines describing the flight connections. Each line has three integers $a$, $b$ and $c$: a flight begins at city $a$, ends at city $b$, and its length is $c$. Each flight is a one-way flight.


You can assume that it is possible to travel from Syrjälä to all other cities.


## Output


Print $n$ integers: the shortest route lengths from Syrjälä to cities $1,2,\dots,n$.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
3 4
1 2 6
1 3 2
3 2 3
1 3 4
```


Output:


```
0 5 2
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
  vector<vector<pi>> edg(n+1); fir(m){
    ll u, v, w; cin>>u>>v>>w;
    edg[u].push_back({v, w});
  }

  vi dp(n+1, inf), vis(n+1);
  dp[1]=0;
  priority_queue<pi> qu; qu.push({0, 1});
  while(sz(qu)){
    auto [d, at]=qu.top(); qu.pop();
    if(vis[at]) continue;
    vis[at]++;
    
    for(auto [to, wt]: edg[at]) if(dp[to]>dp[at]+wt){
      dp[to]=dp[at]+wt;
      qu.push({-dp[to], to});
    }
  }
  fir(n) cout<<dp[i+1]<<ln;
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
