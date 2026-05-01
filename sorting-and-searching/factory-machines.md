# Factory Machines

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A factory has $n$ machines which can be used to make products. Your goal is to make a total of $t$ products.


For each machine, you know the number of seconds it needs to make a single product. The machines can work simultaneously, and you can freely decide their schedule.


What is the shortest time needed to make $t$ products?


## Input


The first input line has two integers $n$ and $t$: the number of machines and products.


The next line has $n$ integers $k_1,k_2,\dots,k_n$: the time needed to make a product using each machine.


## Output


Print one integer: the minimum time needed to make $t$ products.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le t \le 10^9$
- $1 \le k_i \le 10^9$


## Example


Input:


```
3 7
3 2 5
```


Output:


```
8
```


Explanation: Machine 1 makes two products, machine 2 makes four products and machine 3 makes one product.



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
  ll n, t; cin>>n>>t;
  vi v(n); fir(n) cin>>v[i];

  ll l=0, r=inf;
  while(l<r){
    ll m=l+(r-l)/2;
    ll c=0; fir(n){
      c+=m/v[i];
      if(c>=t) break;
    }
    if(c<t) l=m+1;
    else r=m;
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
