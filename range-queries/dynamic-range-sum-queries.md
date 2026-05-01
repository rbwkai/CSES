# Dynamic Range Sum Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to process $q$ queries of the following types:



update the value at position $k$ to $u$
what is the sum of values in range $[a,b]$?

## Input


The first input line has two integers $n$ and $q$: the number of values and queries.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the array values.


Finally, there are $q$ lines describing the queries. Each line has three integers: either "$1$ $k$ $u$" or "$2$ $a$ $b$".


## Output


Print the result of each query of type 2.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le x_i, u \le 10^9$
- $1 \le k \le n$
- $1 \le a \le b \le n$


## Example


Input:


```
8 4
3 2 4 5 1 1 5 3
2 1 4
2 5 6
1 3 1
2 1 4
```


Output:


```
14
2
11
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
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;

template <class T> struct indexed_tree{
  ll ss;
  vector<T> bit;

  indexed_tree(ll n): ss(n), bit(n+1, 0) {}

  void update(ll i, ll delta){
    for(++i; i<=ss; i+=i&-i) bit[i]+=delta;
  }
  T query(int i){
    T res=0;
    for(++i; i>0; i-=i&-i) res+=bit[i];
    return res;
  }
  long unsigned int size(){return ss;}
};

void solve(){
  ll n, q; cin>>n>>q;
  vi v(n); fir(n) cin>>v[i];
  indexed_tree<ll> bit(n); fir(n) bit.update(i, v[i]);

  while(q--){
    ll t, a, b; cin>>t>>a>>b;
    a--;
    if(t==1){
      ll d=b-v[a]; v[a]=b;
      bit.update(a, d);
    }else{
      b--;
      cout<<bit.query(b)-bit.query(a-1)<<en;
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
