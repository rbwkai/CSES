# Reachable Nodes

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A directed acyclic graph consists of $n$ nodes and $m$ edges. The nodes are numbered $1,2,\dots,n$.


Calculate for each node the number of nodes you can reach from that node (including the node itself).


## Input


The first input line has two integers $n$ and $m$: the number of nodes and edges.


Then there are $m$ lines describing the edges. Each line has two distinct integers $a$ and $b$: there is an edge from node $a$ to node $b$.


## Output


Print $n$ integers: for each node the number of reachable nodes.


## Constraints


- $1 \le n \le 5 \cdot 10^4$
- $1 \le m \le 10^5$


## Example


Input:


```
5 6
1 2
1 3
1 4
2 3
3 5
4 5
```


Output:


```
5 3 2 2 1
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
  ll n, m; cin>>n>>m;
  grid edg(n+1); fir(m){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
  }

  ll const N = 5e4 + 1;
  bitset<N> msk[N];
  vi vis(n+1), res(n+1);
  function<void(ll)> rec=[&](ll at){
    msk[at].set(at); vis[at]++;
    for(ll to: edg[at]){
      if(!vis[to]) rec(to);
      msk[at]|=msk[to];
    }
    res[at] = msk[at].count();
  };

  fir(n) if(!vis[i+1]) rec(i+1);
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
