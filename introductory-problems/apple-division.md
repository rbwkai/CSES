# Apple Division

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.


## Input


The first input line has an integer $n$: the number of apples.


The next line has $n$ integers $p_1,p_2,\dots,p_n$: the weight of each apple.


## Output


Print one integer: the minimum difference between the weights of the groups.


## Constraints


- $1 \le n \le 20$
- $1 \le p_i \le 10^9$


## Example


Input:


```
5
3 2 7 4 1
```


Output:


```
1
```


Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).



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

  ll res=inf;
  fir(1<<n){
    ll a=0, b=0;
    fjr(n) {
      ((i>>j)&1)? a+=v[j]: b+=v[j];
    }
    res=min(res, abs(a-b));
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
