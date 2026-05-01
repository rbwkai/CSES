# List Removals

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a list consisting of $n$ integers. Your task is to remove elements from the list at given positions, and report the removed elements.


## Input


The first input line has an integer $n$: the initial size of the list. During the process, the elements are numbered $1,2,\dots,k$ where $k$ is the current size of the list.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the list.


The last line has $n$ integers $p_1,p_2,\dots,p_n$: the positions of the elements to be removed.


## Output


Print the elements in the order they are removed.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$
- $1 \le p_i \le n-i+1$


## Example


Input:


```
5
2 6 1 4 2
3 1 3 1 1
```


Output:


```
1 2 2 6 4
```


Explanation: The contents of the list are $[2,6,1,4,2]$, $[2,6,4,2]$, $[6,4,2]$, $[6,4]$, $[4]$ and $[]$.



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
    return max(a, b);
  }

  void lazyapply(T &to, int l, int r, const L &fr){
    if(fr!=-1) to=fr;
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
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];
  ordered_set<ll> st; fir(n) st.insert(i);

  fir(n){
    ll t; cin>>t; t--;
    ll id=*st.find_by_order(t);
    cout<<v[id]<<" ";
    st.erase(id);
  }
  cout<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
