# Subarray Divisibility

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to count the number of subarrays where the sum of values is divisible by $n$.


## Input


The first input line has an integer $n$: the size of the array.


The next line has $n$ integers $a_1,a_2,\dots,a_n$: the contents of the array.


## Output


Print one integer: the required number of subarrays.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $-10^9 \le a_i \le 10^9$


## Example


Input:


```
5
3 1 2 7 4
```


Output:


```
1
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
  vi v(n); fir(n) cin>>v[i];
  map<ll, ll> mp;

  ll sm=0, res=0; mp[0]=1;
  fir(n){
    sm+=v[i]; sm=(sm%n+n)%n; 
    if(mp.find(sm)!=mp.end()) res+=mp[sm];
    mp[sm]++;
  }
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
