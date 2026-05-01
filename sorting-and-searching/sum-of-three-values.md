# Sum of Three Values

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers, and your task is to find three values (at distinct positions) whose sum is $x$.


## Input


The first input line has two integers $n$ and $x$: the array size and the target sum.


The second line has $n$ integers $a_1,a_2,\dots,a_n$: the array values.


## Output


Print three integers: the positions of the values. If there are several solutions, you may print any of them. If there are no solutions, print IMPOSSIBLE.


## Constraints


- $1 \le n \le 5000$
- $1 \le x,a_i \le 10^9$


## Example


Input:


```
4 8
2 7 5 1
```


Output:


```
1 3 4
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


void solve(){
  ll n, x; cin>>n>>x;
  vector<pi> v(n); fir(n) cin>>v[i].first;
  fir(n) v[i].second=i+1;
  sort(v.begin(), v.end());

  fir(n-1) fjr(i){
    ll l=i+1, r=n-1;
    while(l<r){
      ll k=(l+r)/2;
      if(v[i].first+v[j].first+v[k].first<x) l=k+1;
      else r=k;
    }
    if(v[i].first+v[j].first+v[l].first==x){
      cout<<v[i].second<<" "<<v[j].second<<" "<<v[l].second<<en;
      return;
    }
  }
  cout<<"IMPOSSIBLE"<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
