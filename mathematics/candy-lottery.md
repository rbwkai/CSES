# Candy Lottery

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ children, and each of them independently gets a random integer number of candies between $1$ and $k$.


What is the expected maximum number of candies a child gets?


## Input


The only input line contains two integers $n$ and $k$.


## Output


Print the expected number rounded to six decimal places (rounding half to even).


## Constraints


- $1 \le n \le 100$
- $1 \le k \le 100$


## Example


Input:


```
2 3
```


Output:


```
2.444444
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

  double pd=0;
  fir(k){
    pd+=pow(i, n);
  }
  fix(6);
  cout<<(k-pd/pow(k, n))<<en;
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
