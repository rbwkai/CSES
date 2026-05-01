# Nearest Smaller Values

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to find for each array position the nearest position to its left having a smaller value.


## Input


The first input line has an integer $n$: the size of the array.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the array values.


## Output


Print $n$ integers: for each array position the nearest position with a smaller value. If there is no such position, print $0$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
8
2 5 1 4 8 3 2 5
```


Output:


```
0 1 0 3 4 3 3 7
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
  ll n; cin>>n;
  vi v(n+1); fir(n) cin>>v[i+1];
  v[0]=-inf;
  stack<ll> sk; sk.push(0);
  fir(n){
    while(v[sk.top()]>=v[i+1]) sk.pop();
    cout<<sk.top()<<" ";
    sk.push(i+1);
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
