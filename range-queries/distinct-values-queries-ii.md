# Distinct Values Queries II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to process $q$ queries of the following types:



update the value at position $k$ to $u$
check if every value in range $[a, b]$ is distinct

## Input


The first line has two integers $n$ and $q$: the number of values and queries.


The second line has $n$ integers $x_1, x_2,\dots, x_n$: the array values.


Finally, there are $q$ lines describing the queries. Each line has three integers: either "$1$ $k$ $u$" or "$2$ $a$ $b$".


## Output


For each query of type 2, print YES if every value in the range is distinct and NO otherwise.


## Constraints


- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le x_i, u \le 10^9$
- $1 \le k \le n$
- $1 \le a \le b \le n$


## Example


Input:


```
5 4
3 2 7 2 8
2 3 5
2 2 5
1 2 9
2 2 5
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
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define F first
#define S second
#define pb push_back
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)



// 一心不乱
ll const N = 1e7;
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
    mint a=b, r=1; for( ; p; p>>=1, a=a*a) if(p&1) r=r*a; return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
};



template <class T>
struct segtree{
  int ss;
  vector<T> tree; 
  T treeidn;

  segtree(int n, T tid):
    ss(n),
    tree(4*n, tid), treeidn(tid) {}

  T merge(const T &a, const T &b){
    return max(a, b);
  }

  void build(int id, int l, int r, const vector<T> &v){
    if(l==r){
      tree[id] = v[l];
      return;
    }
    int m = l+(r-l)/2;
    build(id*2+1, l, m, v);
    build(id*2+2, m+1, r, v);
    tree[id] = merge(tree[id*2+1], tree[id*2+2]);
  }

  T query(int id, int l, int r, int ql, int qr){
    if(ql<=l and r<=qr) return tree[id];
    if(ql>r or qr<l) return treeidn;

    int m = l+(r-l)/2;
    T tl = query(id*2+1, l, m, ql, qr);
    T tr = query(id*2+2, m+1, r, ql, qr);
    return merge(tl, tr);
  }

  void update(int id, int l, int r, int idx, T val){
    if(l==r){
      tree[id] = val;
      return;
    }
    int m = l+(r-l)/2;
    if(idx<=m)
      update(id*2+1, l, m, idx, val);
    else
      update(id*2+2, m+1, r, idx, val);
    
    tree[id] = merge(tree[id*2+1], tree[id*2+2]);
  }

  void update(int idx, T val){
    update(0, 0, ss-1, idx, val);
  }
  void build(const vector<T> &v){
    build(0, 0, ss-1, v);
  }
  T query(int ql, int qr){
    return query(0, 0, ss-1, ql, qr);
  }
};
void solve(){
  ll n, Q; cin>>n>>Q;
  gp_hash_table<ll, set<ll>> pos;
  vi v(n); fir(n) cin>>v[i], pos[v[i]].insert(i);

  map<ll, ll> f;
  vi lo(n); fir(n) lo[i] = (f.count(v[i])? f[v[i]]: -1), f[v[i]]=i; 

  segtree<ll> seg(n, -inf);
  seg.build(lo);
  fir(Q){
    ll t, x, y; cin>>t>>x>>y;
    if(t==1){
      x--;
      ll p = v[x]; auto np = pos[p].upper_bound(x);
      if(np!=pos[p].end()) lo[*np] = lo[x], seg.update(*np, lo[x]);

      ll q = y; auto nq = pos[q].upper_bound(x);
      if(nq!=pos[q].end()) lo[*nq] = x, seg.update(*nq, x);

      auto r = pos[q].lower_bound(x);
      ll uv = (r!=pos[q].begin()? *prev(r): -1);
      lo[x] = uv;
      seg.update(x, uv);

      pos[p].erase(x); v[x] = y;
      pos[y].insert(x);
    }
    if(t==2){
      x--; y--;
      ll mi = seg.query(x, y);
      cout<<(mi<x? "YES": "NO")<<en;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
