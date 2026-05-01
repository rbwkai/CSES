# Common Divisors

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ positive integers. Your task is to find two integers such that their greatest common divisor is as large as possible.


## Input


The first input line has an integer $n$: the size of the array.


The second line has $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


## Output


Print the maximum greatest common divisor.


## Constraints


- $2 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^6$


## Example


Input:


```
5
3 14 15 7 9
```


Output:


```
7
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
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

void solve(){
  ll n, N=1e6; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  vi dp(N+6);
  fir(n) dp[v[i]]++;

  for(int i=N; i; i--){
    ll cn=0;
    for(int j=i; j<=N; j+=i) cn+=dp[j];

    if(cn>1){
      cout<<i<<en;
      return;
    }
  }
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
