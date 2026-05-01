# Maximum Subarray Sum II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to find the maximum sum of values in a contiguous subarray with length between $a$ and $b$.


## Input


The first input line has three integers $n$, $a$ and $b$: the size of the array and the minimum and maximum subarray length.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the array values.


## Output


Print one integer: the maximum subarray sum.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a \le b \le n$
- $-10^9 \le x_i \le 10^9$


## Example


Input:


```
8 1 2
-1 3 -2 5 3 -5 2 2
```


Output:


```
8
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
  ll n, a, b; cin>>n>>a>>b;
  vi v(n); fir(n) cin>>v[i];
  vi ps(n+1); fir(n) ps[i+1]=ps[i]+v[i];

  ll res=-inf;
  multiset<ll> st;
  fir(n+1) if(i>=a){
    st.insert(ps[i-a]);
    if(i>b) st.erase(st.find(ps[i-b-1]));
    res=max(res, ps[i]-*st.begin());
  }
  cout<<res<<en;
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
