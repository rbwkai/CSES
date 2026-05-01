# Subarray Sums I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ positive integers, your task is to count the number of subarrays having sum $x$.


## Input


The first input line has two integers $n$ and $x$: the size of the array and the target sum $x$.


The next line has $n$ integers $a_1,a_2,\dots,a_n$: the contents of the array.


## Output


Print one integer: the required number of subarrays.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x,a_i \le 10^9$


## Example


Input:


```
5 7
2 4 1 2 7
```


Output:


```
3
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
  ll n, k; cin>>n>>k;
  vi v(n+1); fir(n) cin>>v[i];

  ll res=0, lf=0, rt=-1, sm=0;
  while(1){
    if(sm<k or lf>rt) sm+=v[++rt];
    else sm-=v[lf++];
     
    if(rt==n or lf==n) break;
    if(sm==k) res++;
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
