# Reachability Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A directed graph consists of $n$ nodes and $m$ edges. The edges are numbered $1,2,\dots,n$.


Your task is to answer $q$ queries of the form "can you reach node $b$ from node $a$?"


## Input


The first input line has three integers $n$, $m$ and $q$: the number of nodes, edges and queries.


Then there are $m$ lines describing the edges. Each line has two distinct integers $a$ and $b$: there is an edge from node $a$ to node $b$.


Finally there are $q$ lines describing the queries. Each line consists of two integers $a$ and $b$: "can you reach node $b$ from node $a$?"


## Output


Print the answer for each query: either "YES" or "NO".


## Constraints


- $1 \le n \le 5 \cdot 10^4$
- $1 \le m,q \le 10^5$


## Example


Input:


```
4 4 3
1 2
2 3
3 1
4 3
1 3
1 4
4 1
```


Output:


```
YES
NO
YES
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
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

struct mint{
  ll v; 
  mint(ll _v=0) {v = (_v%mod +mod)%mod;}

  friend mint operator+(const mint& a, const mint& b){ return mint(a.v + b.v); }
  friend mint operator-(const mint& a, const mint& b){ return mint(a.v - b.v); }
  friend mint operator*(const mint& a, const mint& b){ return mint(a.v * b.v); }
  friend mint operator/(const mint& a, const mint& b){ return a*minv(b); }
  friend mint mpow(const mint& b, ll p){
    mint a=b, r=1;
    for( ; p; p>>=1, a=a*a) if(p&1) r=r*a;
    return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
};

void solve(){
  ll n, m, q; cin>>n>>m>>q;
  grid edg(n+1); fir(m){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
  }

  ll tm = 1;
  vi scc(n+1), idx(n+1, -1), mnv(n+1);
  stack<ll> sk;
  function<void(ll)> rec=[&](ll at){
    idx[at]=tm++; mnv[at]=idx[at];
    sk.push(at);

    for(ll to: edg[at]) if(idx[to]){
      if(idx[to] != -1) mnv[at]=min(idx[to], mnv[at]); 
      else{
        rec(to);
        mnv[at]=min(mnv[at], mnv[to]);
      }
    }

    if(idx[at]==mnv[at]) while(1){
      ll cr = sk.top(); sk.pop();
      scc[cr] = at; idx[cr]=0;
      if(cr==at) break;
    }
  }; fir(n) if(idx[i+1]==-1) rec(i+1);
  
  vector<set<ll>> cmp(n+1);
  for(int u=1; u<=n; u++){
    for(int v: edg[u]){
      cmp[scc[u]].insert(scc[v]);
    }
  }

  ll const N = 5e4+4;
  bitset<N> msk[N];
  vi vis(n+1);
  function<void(ll)> pre = [&](ll at){
    msk[at].set(at); vis[at]++;
    for(ll to: cmp[at]){
      if(!vis[to]) pre(to);
      msk[at] |= msk[to];
    }
  }; fir(n) if(!vis[i+1]) pre(i+1);

  while(q--){
    ll a, b; cin>>a>>b;
    cout<<(msk[scc[a]][scc[b]]? "YES": "NO")<<en;
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
