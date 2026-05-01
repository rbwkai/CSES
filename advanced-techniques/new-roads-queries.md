# New Roads Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ cities in Byteland but no roads between them. However, each day, a new road will be built. There will be a total of $m$ roads.


Your task is to process $q$ queries of the form: "after how many days can we travel from city $a$ to city $b$ for the first time?"


## Input


The first input line has three integers $n$, $m$ and $q$: the number of cities, roads and queries. The cities are numbered $1,2,\dots,n$.


After this, there are $m$ lines that describe the roads in the order they are built. Each line has two integers $a$ and $b$: there will be a road between cities $a$ and $b$.


Finally, there are $q$ lines that describe the queries. Each line has two integers $a$ and $b$: we want to travel from city $a$ to city $b$.


## Output


For each query, print the number of days, or $-1$ if it is never possible.


## Constraints


- $1 \le n, m, q \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 4 3
1 2
2 3
1 3
2 5
1 3
3 4
3 5
```


Output:


```
2
-1
4
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
 
ll const N = 2e6+6;
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

void solve(){
  ll n, m, q; cin>>n>>m>>q;
  grid edg(m+2, vi(2)); fir(m) cin>>edg[i+1][0]>>edg[i+1][1];
  vector<tuple<ll, ll, ll>> qry(q); fir(q){
    ll a, b; cin>>a>>b;
    qry[i] = {i, a, b};
  }

  vi res(q);
  DSU dsu(n);
  function<void(ll, ll, vector<tuple<ll, ll, ll>>&)> rec 
    = [&](ll l, ll r, vector<tuple<ll, ll, ll>> &qs){
    if(l==r){
      for(auto [id, a, b]: qs) res[id]=l; 
      return;
    }
    
    ll m = (l+r)/2;
    for(int i=l; i<=m; ++i)
      dsu.link(edg[i][0], edg[i][1]);

    vector<tuple<ll, ll, ll>> L, R;
    for(auto [id, a, b]: qs){
      if(dsu.root(a)!=dsu.root(b)) R.push_back({id, a, b});
      else L.push_back({id, a, b});
    }

    rec(m+1, r, R);
    for(int i=l; i<=m; ++i) dsu.undo();
    rec(l, m, L);
  }; rec(0, m+1, qry);

  fir(q) cout<<(res[i]==m+1? -1: res[i])<<en;
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
