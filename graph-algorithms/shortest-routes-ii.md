# Shortest Routes II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ cities and $m$ roads between them. Your task is to process $q$ queries where you have to determine the length of the shortest route between two given cities.


## Input


The first input line has three integers $n$, $m$ and $q$: the number of cities, roads, and queries.


Then, there are $m$ lines describing the roads. Each line has three integers $a$, $b$ and $c$: there is a road between cities $a$ and $b$ whose length is $c$. All roads are two-way roads.


Finally, there are $q$ lines describing the queries. Each line has two integers $a$ and $b$: determine the length of the shortest route between cities $a$ and $b$.


## Output


Print the length of the shortest route for each query. If there is no route, print $-1$ instead.


## Constraints


- $1 \le n \le 500$
- $1 \le m \le n^2$
- $1 \le q \le 10^5$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
4 3 5
1 2 5
1 3 9
2 3 3
1 2
2 1
1 3
1 4
3 2
```


Output:


```
5
5
8
-1
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
#define fkr(_O) for(int k=0, kk=_O-1; k<_O; ++k, --kk)
 
ll const inf = 0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, m, q; cin>>n>>m>>q;

  grid dp(n+1, vi(n+1, 1e18)); 
  fir(n) dp[i+1][i+1]=0;
  grid edg(n+1); fir(m){
    ll u, v, w; cin>>u>>v>>w;
    dp[u][v]=min(dp[u][v], w);
    dp[v][u]=dp[u][v];
  }
  
  fkr(n) fjr(n) fir(n)
    dp[j+1][i+1]=min(dp[j+1][i+1], dp[j+1][k+1]+dp[k+1][i+1]);

  while(q--){
    ll a, b; cin>>a>>b;
    cout<<(dp[a][b]>=inf? -1: dp[a][b])<<en;
  }
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
