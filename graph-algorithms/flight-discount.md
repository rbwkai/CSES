# Flight Discount

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to find a minimum-price flight route from Syrjälä to Metsälä. You have one discount coupon, using which you can halve the price of any single flight during the route. However, you can only use the coupon once.


When you use the discount coupon for a flight whose price is $x$, its price becomes $\lfloor x/2 \rfloor$ (it is rounded down to an integer).


## Input


The first input line has two integers $n$ and $m$: the number of cities and flight connections. The cities are numbered $1,2,\ldots,n$. City 1 is Syrjälä, and city $n$ is Metsälä.


After this there are $m$ lines describing the flights. Each line has three integers $a$, $b$, and $c$: a flight begins at city $a$, ends at city $b$, and its price is $c$. Each flight is unidirectional.


You can assume that it is always possible to get from Syrjälä to Metsälä.


## Output


Print one integer: the price of the cheapest route from Syrjälä to Metsälä.


## Constraints


- $2 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
3 4
1 2 3
2 3 1
1 3 7
2 1 5
```


Output:


```
2
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

  grid dp(n+1, vi(2, inf)), vis(n+1, vi(2));
  dp[1][0]=0;
  priority_queue<pair<ll, pi>> qu; qu.push({0, {1, 0}});
  while(sz(qu)){
    auto [d, p]=qu.top(); qu.pop();
    auto [at, cs]=p;
    if(vis[at][cs]) continue;
    vis[at][cs]++;
    
    for(auto [to, wt]: edg[at]) if(dp[to][cs]>dp[at][cs]+wt){
      dp[to][cs]=dp[at][cs]+wt;
      qu.push({-dp[to][cs], {to, cs}});
    }

    if(!cs) for(auto [to, wt]: edg[at]) if(dp[to][1]>dp[at][0]+wt/2){
      dp[to][1]=dp[at][0]+wt/2;
      qu.push({-dp[to][1], {to, 1}});
    }
  }
  cout<<dp[n][1]<<en;
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
