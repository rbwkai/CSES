# Nested Ranges Check

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given $n$ ranges, your task is to determine for each range if it contains some other range and if some other range contains it.


Range $[a,b]$ contains range $[c,d]$ if $a \le c$ and $d \le b$.


## Input


The first input line has an integer $n$: the number of ranges.


After this, there are $n$ lines that describe the ranges. Each line has two integers $x$ and $y$: the range is $[x,y]$.


You may assume that no range appears more than once in the input.


## Output


First print a line that describes for each range (in the input order) if it contains some other range (1) or not (0).


Then print a line that describes for each range (in the input order) if some other range contains it (1) or not (0).


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x < y \le 10^9$


## Example


Input:


```
4
1 6
2 4
4 8
3 6
```


Output:


```
1 0 0 0
0 1 0 1
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
//less_equal for multiset. bounds are swapped.
#define en "\n"
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = LLONG_MAX-3e5; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  ll n; cin>>n;
  grid v(n, vi(3)); fir(n){
    ll a, b; cin>>a>>b;
    v[i]={b, -a, i};
  } sort(v.begin(), v.end());

  ordered_set<ll> fl, bl;
  grid res(2, vi(n));
  fir(n){
    auto ft=fl.upper_bound(-v[i][1]);
    ll fd=sz(fl); if(ft!=fl.end()) fd=fl.order_of_key(*ft);
    res[0][v[i][2]]=sz(fl)-fd;
    fl.insert(-v[i][1]);

    auto bt=bl.lower_bound(-v[n-i-1][1]);
    ll bd=sz(bl); if(bt!=bl.end()) bd=bl.order_of_key(*bt);
    res[1][v[n-i-1][2]]=bd;
    bl.insert(-v[n-i-1][1]);
  }
  fir(2){
    fjr(n) cout<<(res[i][j]>0)<<" ";
    cout<<en;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
