# Stick Lengths

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ sticks with some lengths. Your task is to modify the sticks so that each stick has the same length.


You can either lengthen and shorten each stick. Both operations cost $x$ where $x$ is the difference between the new and original length.


What is the minimum total cost?


## Input


The first input line contains an integer $n$: the number of sticks.


Then there are $n$ integers: $p_1,p_2,\ldots,p_n$: the lengths of the sticks.


## Output


Print one integer: the minimum total cost.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le p_i \le 10^9$


## Example


Input:


```
5
2 3 1 5 2
```


Output:


```
5
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
  sort(v.begin(), v.end());

  ll m=v[n/2], res=0;
  fir(n) res+=abs(m-v[i]);
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
