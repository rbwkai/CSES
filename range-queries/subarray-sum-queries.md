# Subarray Sum Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is an array consisting of $n$ integers. Some values of the array will be updated, and after each update, your task is to report the maximum subarray sum in the array.


## Input


The first input line contains integers $n$ and $m$: the size of the array and the number of updates. The array is indexed $1,2,\ldots,n$.


The next line has $n$ integers: $x_1,x_2,\ldots,x_n$: the initial contents of the array.


Then there are $m$ lines describing the changes. Each line has two integers $k$ and $x$: the value at position $k$ becomes $x$.


## Output


After each update, print the maximum subarray sum. Empty subarrays (with sum $0$) are allowed.


## Constraints


- $1 \le n, m \le 2 \cdot 10^5$
- $-10^9 \le x_i \le 10^9$
- $1 \le k \le n$
- $-10^9 \le x \le 10^9$


## Example


Input:


```
5 3
1 2 -3 5 -1
2 6
3 1
2 -2
```


Output:


```
9
13
6
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
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;

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
    st.update(a-1, a-1, b);
    cout<<st.query(0, n-1).rs<<en;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
