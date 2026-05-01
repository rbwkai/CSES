# Investigation

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are going to travel from Syrjälä to Lehmälä by plane. You would like to find answers to the following questions:


- what is the minimum price of such a route?
- how many minimum-price routes are there? (modulo $10^9+7)$
- what is the minimum number of flights in a minimum-price route?
- what is the maximum number of flights in a minimum-price route?


## Input


The first input line contains two integers $n$ and $m$: the number of cities and the number of flights. The cities are numbered $1,2,\ldots,n$. City 1 is Syrjälä, and city $n$ is Lehmälä.


After this, there are $m$ lines describing the flights. Each line has three integers $a$, $b$, and $c$: there is a flight from city $a$ to city $b$ with price $c$. All flights are one-way flights.


You may assume that there is a route from Syrjälä to Lehmälä.


## Output


Print four integers according to the problem statement.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
4 5
1 4 5
1 2 4
2 4 5
1 3 2
3 4 3
```


Output:


```
5 2 1 2
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
 
  vi vis(n+1);
  vi dis(n+1), mxe(n+1), mne(n+1), cnt(n+1);
  dis[1]=0, mxe[1]=0, mne[1]=0, cnt[1]=1;
  priority_queue<pi> qu; qu.push({0, 1});
  while(sz(qu)){
    auto [d, at]=qu.top(); qu.pop();
    if(vis[at]) continue;
    vis[at]++;
    
    for(auto [to, wt]: edg[at]){
      if(dis[to]>dis[at]+wt){
        dis[to] = dis[at]+wt;
        mxe[to] = mxe[at]+1;
        mne[to] = mne[at]+1;
        cnt[to] = cnt[at];
        qu.push({-dp[to], to});
      }
      else if(dis[to]==dis[at]+wt){
        mxe[to] = max(mxe[to], mxe[at]+1);
        mne[to] = min(mne[to], mne[at]+1);
        cnt[to] += cnt[at];
      }
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
