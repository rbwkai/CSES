# Counting Tilings

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to count the number of ways you can fill an $n \times m$ grid using $1 \times 2$ and $2 \times 1$ tiles.


## Input


The only input line has two integers $n$ and $m$.


## Output


Print one integer: the number of ways modulo $10^9+7$.


## Constraints


- $1 \le n \le 10$
- $1 \le m \le 1000$


## Example


Input:


```
4 7
```


Output:


```
781
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
  ll n, m; cin>>n>>m;
  grid dp(2, vi(1<<n)); dp[1][0]=1;

  fjr(m) fir(n){
    vi ndp(1<<n);
    for(int m=0; m<(1<<n); ++m){
      ll x=1<<i;
      ndp[m^x]=(ndp[m^x]+dp[1][m])%mod;
      if(i and !(m&x) and !(m&(x>>1))) ndp[m]=(ndp[m]+dp[0][m])%mod;
    }
    swap(dp[0], dp[1]); swap(dp[1], ndp);
  }
  cout<<dp[1][0]<<en;
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
