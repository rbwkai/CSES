# Towers

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given $n$ cubes in a certain order, and your task is to build towers using them. Whenever two cubes are one on top of the other, the upper cube must be smaller than the lower cube.


You must process the cubes in the given order. You can always either place the cube on top of an existing tower, or begin a new tower. What is the minimum possible number of towers?


## Input


The first input line contains an integer $n$: the number of cubes.


The next line contains $n$ integers $k_1,k_2,\ldots,k_n$: the sizes of the cubes.


## Output


Print one integer: the minimum number of towers.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le k_i \le 10^9$


## Example


Input:


```
5
3 8 2 1 5
```


Output:


```
2
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

ll const inf = LLONG_MAX-3e5; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];
  multiset<ll> st;

  fir(n){
    if(st.upper_bound(v[i])==st.end()) st.insert(v[i]);
    else{
      auto it=st.upper_bound(v[i]);
      st.erase(it);
      st.insert(v[i]);
    }
  }
  cout<<sz(st)<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
