# Collecting Numbers

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array that contains each number between $1 \dots n$ exactly once. Your task is to collect the numbers from $1$ to $n$ in increasing order.


On each round, you go through the array from left to right and collect as many numbers as possible. What will be the total number of rounds?


## Input


The first line has an integer $n$: the array size.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the numbers in the array.


## Output


Print one integer: the number of rounds.


## Constraints


- $1 \le n \le 2 \cdot 10^5$


## Example


Input:


```
5
4 2 1 5 3
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
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = LLONG_MAX-3e5; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  ll n; cin>>n;
  vi v(n); fir(n){
    ll t; cin>>t;
    v[t-1]=i;
  }

  ll c=1;
  fir(n-1) if(v[i]>v[i+1]) c++;
  cout<<c<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
