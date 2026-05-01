# Round Trip

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Byteland has $n$ cities and $m$ roads between them. Your task is to design a round trip that begins in a city, goes through two or more other cities, and finally returns to the starting city. Every intermediate city on the route has to be distinct.


## Input


The first input line has two integers $n$ and $m$: the number of cities and roads. The cities are numbered $1,2,\dots,n$.


Then, there are $m$ lines describing the roads. Each line has two integers $a$ and $b$: there is a road between those cities.


Every road is between two different cities, and there is at most one road between any two cities.


## Output


First print an integer $k$: the number of cities on the route. Then print $k$ cities in the order they will be visited. You can print any valid solution.


If there are no solutions, print "IMPOSSIBLE".


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 6
1 3
1 2
5 3
1 5
2 4
4 5
```


Output:


```
4
3 5 1 3
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
    edg[v].push_back(u);
  }

  vi vis(n+1), par(n+1);
  function<ll(ll)> dfs=[&](ll at){
    vis[at]=1;
    for(ll to: edg[at]){
      if(vis[to]>1 or par[at]==to) continue;
      if(vis[to]==1 and par[at]!=to){
        vis[to]=3; return at;
      }
      par[to]=at;
      ll d = dfs(to);
      if(d) return d;
    }
    if(vis[at]==1) vis[at]=2;
    return 0LL;
  };
  
  ll d=0;
  fir(n) if(d=dfs(i+1)) break;
  if(!d) {cout<<"IMPOSSIBLE"<<en; return;}

  vi res={d};
  while(vis[d]!=3) res.push_back(d=par[d]);
  res.push_back(res[0]); 

  cout<<sz(res)<<en;
  fir(sz(res)) cout<<res[i]<<" ";
  cout<<en;
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
