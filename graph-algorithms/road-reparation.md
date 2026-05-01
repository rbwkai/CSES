# Road Reparation

**Time limit: 1.00 s**  
**Memory limit: 128 MB**

---

## Problem

There are $n$ cities and $m$ roads between them. Unfortunately, the condition of the roads is so poor that they cannot be used. Your task is to repair some of the roads so that there will be a decent route between any two cities.


For each road, you know its reparation cost, and you should find a solution where the total cost is as small as possible.


## Input


The first input line has two integers $n$ and $m$: the number of cities and roads. The cities are numbered $1,2,\dots,n$.


Then, there are $m$ lines describing the roads. Each line has three integers $a$, $b$ and $c$: there is a road between cities $a$ and $b$, and its reparation cost is $c$. All roads are two-way roads.


Every road is between two different cities, and there is at most one road between two cities.


## Output


Print one integer: the minimum total reparation cost. However, if there are no solutions, print "IMPOSSIBLE".


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
5 6
1 2 3
2 3 5
2 4 2
3 4 8
5 1 7
5 4 4
```


Output:


```
14
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
//#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, m; cin>>n>>m;
  vector<vector<pi>> edg(n+1); fir(m){
    ll u, v, w; cin>>u>>v>>w;
    edg[u].push_back({v, w});
    edg[v].push_back({u, w});
  }
  vi inc(n+1); ll sz=0, res=0;
  priority_queue<pi> pq; pq.push({0, 1});
  while(sz(pq)){
    auto [wx, at]=pq.top(); pq.pop();
    if(inc[at]) continue;

    inc[at]=1, sz++, res-=wx;
    for(auto [to, wt]: edg[at]) if(!inc[to]){
      pq.push({-wt, to});
    }
  }
  if(sz!=n) cout<<"IMPOSSIBLE"<<en;
  else cout<<res<<en;
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
