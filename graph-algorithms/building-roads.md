# Building Roads

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Byteland has $n$ cities, and $m$ roads between them. The goal is to construct new roads so that there is a route between any two cities.


Your task is to find out the minimum number of roads required, and also determine which roads should be built.


## Input


The first input line has two integers $n$ and $m$: the number of cities and roads. The cities are numbered $1,2,\dots,n$.


After that, there are $m$ lines describing the roads. Each line has two integers $a$ and $b$: there is a road between those cities.


A road always connects two different cities, and there is at most one road between any two cities.


## Output


First print an integer $k$: the number of required roads.


Then, print $k$ lines that describe the new roads. You can print any valid solution.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
4 2
1 2
3 4
```


Output:


```
1
2 3
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

  vi vis(n+1);
  function<void(ll)> dfs=[&](ll at){
    vis[at]++;
    for(ll to: edg[at]) if(!vis[to]) dfs(to);
  }; dfs(1);

  vi res;
  fir(n) if(!vis[i+1]) res.push_back(i+1), dfs(i+1);
  cout<<sz(res)<<en;
  fir(sz(res)) cout<<1<<" "<<res[i]<<en;
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
