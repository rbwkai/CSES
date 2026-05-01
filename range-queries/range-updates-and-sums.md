# Range Updates and Sums

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to maintain an array of $n$ values and efficiently process the following types of queries:



Increase each value in range $[a,b]$ by $x$.
Set each value in range $[a,b]$ to $x$.
Calculate the sum of values in range $[a,b]$.

## Input


The first input line has two integers $n$ and $q$: the array size and the number of queries.


The next line has $n$ values $t_1,t_2,\dots,t_n$: the initial contents of the array.


Finally, there are $q$ lines describing the queries. The format of each line is one of the following: "1 $a$ $b$ $x$",  "2 $a$ $b$ $x$", or "3 $a$ $b$".


## Output


Print the answer to each sum query.


## Constraints


- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le t_i, x \le 10^6$
- $1 \le a \le b \le n$


## Example


Input:


```
6 5
2 3 1 1 5 3
3 3 5
1 2 4 2
3 3 5
2 2 4 5
3 3 5
```


Output:


```
7
11
15
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

template <class T, class L> struct segment_tree{
  int ss;
  vector<T> tree; T treeidn;
  vector<L> lazy; L lazyidn;

  segment_tree(int n, T tid, L lid):
    ss(n),
    tree(4*n, tid), treeidn(tid),
    lazy(4*n, lid), lazyidn(lid) {}

  T merge(const T &a, const T &b){
    return a+b;
  }

  void lazyapply(T &to, int l, int r, const L &fr){
    to=to*fr.first+(r-l+1)*fr.second;
  }

  void lazymerge(L &to, const L &fr){
    pi res;
    res.first=to.first*fr.first;
    res.second=to.second*fr.first+fr.second;
    to=res;
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
  segment_tree<ll, pi> st(n, 0, {1, 0});
  st.build(v);

  while(q--){
    ll t; cin>>t;
    if(t==1){
      ll a, b, u; cin>>a>>b>>u;
      st.update(a-1, b-1, {1, u});
    }
    if(t==2){
      ll a, b, u; cin>>a>>b>>u;
      st.update(a-1, b-1, {0, u});
    }
    if(t==3){
      ll a, b; cin>>a>>b;
      cout<<st.query(a-1, b-1)<<en;
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
