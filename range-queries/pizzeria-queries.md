# Pizzeria Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ buildings on a street, numbered $1,2,\dots,n$. Each building has a pizzeria and an apartment.


The pizza price in building $k$ is $p_k$. If you order a pizza from building $a$ to building $b$, its price (with delivery) is $p_a+|a-b|$.


Your task is to process two types of queries:



The pizza price $p_k$ in building $k$ becomes $x$.
You are in building $k$ and want to order a pizza. What is the minimum price?

## Input


The first input line has two integers $n$ and $q$: the number of buildings and queries.


The second line has $n$ integers $p_1,p_2,\dots,p_n$: the initial pizza price in each building.


Finally, there are $q$ lines that describe the queries. Each line is either "1 $k$ $x$" or "2 $k$".


## Output


Print the answer for each query of type 2.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le p_i, x \le 10^9$
- $1 \le k \le n$


## Example


Input:


```
6 3
8 6 4 5 7 5
2 2
1 5 1
2 2
```


Output:


```
5
4
```


---

## Solution

```cpp
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
ll const mod = 998244353; //1e9+7


template <class T, class L> struct segment_tree{
  int ss;
  vector<T> tree; T treeidn;
  vector<L> lazy; L lazyidn;

  segment_tree(int n, T tid, L lid):
    ss(n),
    tree(4*n, tid), treeidn(tid),
    lazy(4*n, lid), lazyidn(lid) {}

  T merge(const T &a, const T &b){
    pi res;
    res.first=min(a.first, b.first);
    res.second=min(a.second, b.second);
    return res;
  }

  void lazyapply(T &to, int l, int r, const L &fr){
    if(fr!=-1){
      to.first=fr+l;
      to.second=fr-l;
    }
  }

  void lazymerge(L &to, const L &fr){
    if(fr!=-1) to=fr;
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
  vector<pi> nd(n); fir(n){
    nd[i].first=v[i]+i;
    nd[i].second=v[i]-i;
  }
  segment_tree<pi, ll> st(n, {inf, inf}, -1);
  st.build(nd);

  while(q--){
    ll t; cin>>t;
    if(t==1){
      ll a, b; cin>>a>>b;
      st.update(a-1, a-1, b);
    }
    else{
      ll k; cin>>k; k--;
      ll up=st.query(k, n-1).first-k;
      ll dw=st.query(0, k).second+k;
      cout<<min(up, dw)<<en;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
