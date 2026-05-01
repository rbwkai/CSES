# Gray Code

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A Gray code is a list of all $2^n$ bit strings of length $n$, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).


Your task is to create a Gray code for a given length $n$.


## Input


The only input line has an integer $n$.


## Output


Print $2^n$ lines that describe the Gray code. You can print any valid solution.


## Constraints


- $1 \le n \le 16$


## Example


Input:


```
2
```


Output:


```
00
01
11
10
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
  vi v(n, 0);

  function<void(ll)> rec=[&](ll i){
    if(i==n){
      fir(n) cout<<v[i];
      cout<<en;
      return;
    }
    rec(i+1);

    v[i]^=1;
    rec(i+1);
  };
  rec(0);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
