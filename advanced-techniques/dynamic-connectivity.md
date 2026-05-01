# Dynamic Connectivity

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider an undirected graph that consists of $n$ nodes and $m$ edges. There are two types of events that can happen:



A new edge is created between nodes $a$ and $b$.
An existing edge between nodes $a$ and $b$ is removed.

Your task is to report the number of components after every event.


## Input


The first input line has three integers $n$, $m$ and $k$: the number of nodes, edges and events.


After this there are $m$ lines describing the edges. Each line has two integers $a$ and $b$: there is an edge between nodes $a$ and $b$. There is at most one edge between any pair of nodes.


Then there are $k$ lines describing the events. Each line has the form "$t$ $a$ $b$" where $t$ is 1 (create a new edge) or 2 (remove an edge). A new edge is always created between two nodes that do not already have an edge between them, and only existing edges can get removed.


## Output


Print $k+1$ integers: first the number of components before the first event, and after this the new number of components after each event.


## Constraints


- $2 \le n \le 10^5$
- $1 \le m,k \le 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 3 3
1 4
2 3
3 5
1 2 5
2 3 5
1 1 2
```


Output:


```
2 2 2 1
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
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

struct DSU{
  vi par, rnk;
  ll cc;
  stack<pi> stk;
  
  DSU(ll n):
    par(n+1), rnk(n+1),
    cc(n){
    fir(n+1) par[i]=i, rnk[i]=1;
  }

  ll root(ll x) {return (par[x]==x? x: root(par[x]));}
  void link(ll x, ll y){
    x=root(x), y=root(y);
    if(x==y) {stk.push({-1, -1}); return;}

    if(rnk[x]<rnk[y]) swap(x, y);
    par[y]=x; rnk[x]+=rnk[y];
    stk.push({x, y}); cc--;
  }
  void undo(){
    auto [x, y]=stk.top(); stk.pop();
    if(x==-1) return;

    par[y]=y; rnk[x]-=rnk[y];
    cc++;
  }
};

struct segtree{
  vector<vector<pi>> tree;

  segtree(ll n): tree(4*n) {}
  
  void add(ll id, ll l, ll r, ll ql, ll qr, pi e){
    if(ql>r or qr<l) return;
    if(ql<=l and r<=qr){
      tree[id].push_back(e); 
      return;
    } 

    ll m = (l+r)/2;
    add(2*id+1, l, m, ql, qr, e);
    add(2*id+2, m+1, r, ql, qr, e);
  }
};

void solve(){
  ll n, m, k; cin>>n>>m>>k;

  map<pi, ll> st;
  segtree seg(k+1);
  fir(m){
    ll u, v; cin>>u>>v; if(u>v) swap(u, v);
    st[{u, v}] = 0;
  }
  fir(k){
    ll t, u, v; cin>>t>>u>>v; if(u>v) swap(u, v);
    if(t==1) st[{u, v}] = i+1;
    if(t==2) {
      seg.add(0, 0, k, st[{u, v}], i, {u, v});
      st.erase({u, v});
    }
  }
  for(auto [e, s]: st) seg.add(0, 0, k, s, k, e);

  DSU dsu(n);
  vi res(k+1);
  function<void(ll, ll, ll)> dfs = [&](ll id, ll l, ll r){
    for(auto [x, y]: seg.tree[id]) dsu.link(x, y);

    if(l == r){
      res[l] = dsu.cc;
    } else {
      ll m = (l+r)/2; 
      dfs(2*id+1, l, m);
      dfs(2*id+2, m+1, r);
    }
    for(auto [x, y]: seg.tree[id]) dsu.undo();
  }; dfs(0, 0, k);

  fir(k+1) cout<<res[i]<<" ";
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
