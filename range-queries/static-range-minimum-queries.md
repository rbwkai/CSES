# Static Range Minimum Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to process $q$ queries of the form: what is the minimum value in range $[a,b]$?


## Input


The first input line has two integers $n$ and $q$: the number of values and queries.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the array values.


Finally, there are $q$ lines describing the queries. Each line has two integers $a$ and $b$: what is the minimum value in range $[a,b]$?


## Output


Print the result of each query.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$
- $1 \le a \le b \le n$


## Example


Input:


```
8 4
3 2 4 5 1 1 5 3
2 4
5 6
1 8
3 3
```


Output:


```
2
1
1
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
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, q; cin>>n>>q;
  vi v(n); fir(n) cin>>v[i];

  vi seg(4*n, inf);
  function<void(ll, ll, ll)> build=[&](ll nd, ll l, ll r){
    if(l==r){
      seg[nd]=v[l];
      return;
    }
    ll m=(l+r)/2;
    build(nd*2+1, l, m);
    build(nd*2+2, m+1, r);
    seg[nd]=min(seg[nd*2+1], seg[nd*2+2]);
  }; build(0, 0, n-1);

  function<ll(ll, ll, ll, ll, ll)> query=[&](ll nd, ll l, ll r, ll ql, ll qr){
    if(r<ql or l>qr) return inf;
    if(ql<=l and r<=qr) return seg[nd];

    ll m=(l+r)/2;
    return min(query(nd*2+1, l, m, ql, qr), query(nd*2+2, m+1, r, ql, qr));
  };
  while(q--){
    ll p, q; cin>>p>>q;
    cout<<query(0, 0, n-1, p-1, q-1)<<en;
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
