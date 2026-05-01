# Subarray Sum Queries II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers and $q$ queries. In each query, your task is to calculate the maximum subarray sum in the range $[a,b]$.


Empty subarrays (with sum $0$) are allowed.


## Input


The first line contains two integers $n$ and $q$: the number of elements and the number of queries.


Then there are $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


Finally there are $q$ lines that describe the queries. Each line has two integers $a$ and $b$.


## Output


Print the answer for each query.


## Constraints


- $1 \le n, q\le 2 \cdot 10^5$
- $-10^9 \le x_i \le 10^9$
- $1 \le a \le b \le n$


## Example


Input:


```
8 4
2 5 1 -2 3 -1 -7 1
2 4
2 5
6 7
4 8
```


Output:


```
6
7
0
3
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

struct node{
  ll sm;
  ll pf;
  ll sf;
  ll rs;
};
template <class T, class L> struct segment_tree{
  int ss;
  vector<T> tree; T treeidn;
  vector<L> lazy; L lazyidn;

  segment_tree(int n, T tid, L lid):
    ss(n),
    tree(4*n, tid), treeidn(tid),
    lazy(4*n, lid), lazyidn(lid) {}

  T merge(const T &a, const T &b){
    node res;
    res.sm=a.sm+b.sm;
    res.pf=max(a.pf, a.sm+b.pf);
    res.sf=max(b.sf, a.sf+b.sm);
    res.rs=max(a.sf+b.pf, max(a.rs, b.rs));
    return res;
  }

  void lazyapply(T &to, int l, int r, const L &fr){
    if(fr!=lazyidn) to={fr, max(0LL, fr), max(0LL, fr), max(0LL, fr)};
  }

  void lazymerge(L &to, const L &fr){
    if(fr!=lazyidn) to=fr;
  }

  bool discriminant(const T &tl, const T &x){
    return tl<x;
  }

  void build(int id, int l, int r, const vector<T> &v){
    if(l==r){
      tree[id]=v[l];
      lazy[id]=lazyidn;
      return;
    }
    int m=l+(r-l)/2;
    build(id*2+1, l, m, v);
    build(id*2+2, m+1, r, v);
    tree[id] = merge(tree[id*2+1], tree[id*2+2]);
    lazy[id] = lazyidn;
  }
  void push(int id, int l, int r){
    if(l!=r) {
      int m=l+(r-l)/2;

      lazyapply(tree[2*id+1], l, m, lazy[id]);
      lazymerge(lazy[2*id+1], lazy[id]);

      lazyapply(tree[2*id+2], m+1, r, lazy[id]);
      lazymerge(lazy[2*id+2], lazy[id]);

      lazy[id] = lazyidn;
    }
  }
  T query(int id, int l, int r, int ql, int qr){
    push(id, l, r);
    if(ql<=l and r<=qr) return tree[id];
    if(ql>r or qr<l) return treeidn;

    int m=l+(r-l)/2;
    T tl = query(id*2+1, l, m, ql, qr);
    T tr = query(id*2+2, m+1, r, ql, qr);
    return merge(tl, tr);
  }
  void update(int id, int l, int r, int ul, int ur, const L &uv) {
    push(id, l, r);
    if (ul<=l and r<=ur) {
      lazyapply(tree[id], l, r, uv);
      lazymerge(lazy[id], uv);
      return;
    }
    if(ul>r or ur<l) return;

    int m=l+(r-l)/2;
    update(id*2+1, l, m, ul, ur, uv);
    update(id*2+2, m+1, r, ul, ur, uv);
    tree[id] = merge(tree[id*2+1], tree[id*2+2]);
  }
  int walk(int id, int l, int r, const T &x){
    if(l==r){
      return l;
    }
    int m=l+(r-l)/2;
    if(discriminant(tree[id*2+1], x)) return walk(id*2+2, m+1, r, x);
    return walk(id*2+1, l, m, x);
  }

  void build(const vector<T> &v){
    build(0, 0, ss-1, v);
  }
  T query(int ql, int qr){
    return query(0, 0, ss-1, ql, qr);
  }
  void update(int ul, int ur, const L &uv){
    update(0, 0, ss-1, ul, ur, uv);
  }
  int walk(const T &x){ //first F
    if(discriminant(tree[0], x)) return ss;
    return walk(0, 0, ss-1, x);
  }
  unsigned long int size(){return ss;}
}; 
 
 
void solve(){
  ll n, q; cin>>n>>q;
  vi v(n); fir(n) cin>>v[i];
  vector<node> vv(n); fir(n) vv[i]={v[i], max(0LL, v[i]), max(0LL, v[i]), max(0LL, v[i])};
  segment_tree<node, ll> st(n, {0, 0, 0, 0}, -inf);
  st.build(vv);

  while(q--){
    ll a, b; cin>>a>>b;
    cout<<st.query(a-1, b-1).rs<<en;
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
