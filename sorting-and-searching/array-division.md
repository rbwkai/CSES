# Array Division

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array containing $n$ positive integers.


Your task is to divide the array into $k$ subarrays so that the maximum sum in a subarray is as small as possible.


## Input


The first input line contains two integers $n$ and $k$: the size of the array and the number of subarrays in the division.


The next line contains $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


## Output


Print one integer: the maximum sum in a subarray in the optimal division.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le k \le n$
- $1 \le x_i \le 10^9$


## Example


Input:


```
5 3
2 4 7 3 5
```


Output:


```
8
```


Explanation: An optimal division is $[2,4],[7],[3,5]$ where the sums of the subarrays are $6,7,8$. The largest sum is the last sum $8$.



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
  vi v(n); fir(n) cin>>v[i];

  ll l=0, r=inf;
  while(l<r){
    ll m=(l+r)/2;
    ll k=1, sm=0;
    fir(n){
      sm+=v[i];
      if(sm>m) k++, sm=v[i];
      if(sm>m) k=x+1;
    }
    if(k<=x) r=m;
    else l=m+1;
  }
  cout<<l<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
