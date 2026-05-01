# Planets and Kingdoms

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A game has $n$ planets, connected by $m$ teleporters. Two planets $a$ and $b$ belong to the same kingdom exactly when there is a route both from $a$ to $b$ and from $b$ to $a$. Your task is to determine for each planet its kingdom.


## Input


The first input line has two integers $n$ and $m$: the number of planets and teleporters. The planets are numbered $1,2,\dots,n$.


After this, there are $m$ lines describing the teleporters. Each line has two integers $a$ and $b$: you can travel from planet $a$ to planet $b$ through a teleporter.


## Output


First print an integer $k$: the number of kingdoms. After this, print for each planet a kingdom label between $1$ and $k$. You can print any valid solution.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 6
1 2
2 3
3 1
3 4
4 5
5 4
```


Output:


```
2
1 1 1 2 2
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

  ll tm=1;
  vi et(n+1, -1), mv(n+1, inf); 
  vi scc(n+1, -1); 
  stack<ll> sk;
  function<void(ll)> dfs=[&](ll at){
    et[at]=tm++; mv[at]=et[at];
    sk.push(at);

    for(ll to: edg[at]) if(et[to]){
      if(et[to]!=-1) mv[at]=min(mv[at], et[to]);
      else{
        dfs(to);
        mv[at]=min(mv[at], mv[to]);
      }
    }

    if(et[at]==mv[at]) while(1){
      ll cr=sk.top(); sk.pop();
      scc[cr]=at; et[cr]=0;
      if(cr==at) break;
    }
  }; fir(n) if(et[i+1]==-1) dfs(i+1);

  map<ll, ll> mp; ll ctr=0;
  vi res(n+1);
  fir(n) res[i+1] = (mp.count(scc[i+1])? mp[scc[i+1]]: mp[scc[i+1]]=++ctr);

  cout<<ctr<<en;
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
