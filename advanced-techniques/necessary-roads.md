# Necessary Roads

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ cities and $m$ roads between them. There is a route between any two cities.


A road is called necessary if there is no route between some two cities after removing that road. Your task is to find all necessary roads.


## Input


The first input line has two integers $n$ and $m$: the number of cities and roads. The cities are numbered $1,2,\dots,n$.


After this, there are $m$ lines that describe the roads. Each line has two integers $a$ and $b$: there is a road between cities $a$ and $b$. There is at most one road between two cities, and every road connects two distinct cities.


## Output


First print an integer $k$: the number of necessary roads. After that, print $k$ lines that describe the roads. You may print the roads in any order.


## Constraints


- $2 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 5
1 2
1 4
2 4
3 5
4 5
```


Output:


```
2
3 5
4 5
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
 
ll const N = 50;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353;

struct mint{
  ll v; 
  mint(ll _v=0) {v = (_v%mod +mod)%mod;}

  friend mint operator+(const mint& a, const mint& b){ return mint(a.v + b.v); }
  friend mint operator-(const mint& a, const mint& b){ return mint(a.v - b.v); }
  friend mint operator*(const mint& a, const mint& b){ return mint(a.v * b.v); }
  friend mint operator/(const mint& a, const mint& b){ return a*minv(b); }
  friend mint mpow(const mint& b, ll p){
    mint a=b, r=1; for( ; p; p>>=1, a=a*a) if(p&1) r=r*a; return r;
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
    edg[v].push_back(u);
  }

  ll tm = 1;
  vi et(n+1, -1), mv(n+1, inf);
  vector<pi> res;
  function<void(ll, ll)> dfs=[&](ll at, ll pr){
    et[at] = mv[at] = tm++;
    for(ll to: edg[at]) if(to!=pr){
      if(et[to]==-1){
        dfs(to, at);
        mv[at] = min(mv[at], mv[to]);
        if(mv[to]>et[at]) res.push_back({at, to});
      }
      else mv[at] = min(mv[at], et[to]);
    }
  };

  fir(n) if(et[i+1]==-1) dfs(i+1, 0);
  cout<<sz(res)<<en;
  for(auto [u, v]: res) cout<<u<<" "<<v<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
