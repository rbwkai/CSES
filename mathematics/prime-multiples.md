# Prime Multiples

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given $k$ distinct prime numbers $a_1,a_2,\ldots,a_k$ and an integer $n$.


Your task is to calculate how many of the first $n$ positive integers are divisible by at least one of the given prime numbers.


## Input


The first input line has two integers $n$ and $k$.


The second line has $k$ prime numbers $a_1,a_2,\ldots,a_k$.


## Output


Print one integer: the number integers within the interval $1,2,\ldots,n$ that are divisible by at least one of the prime numbers.


## Constraints


- $1 \le n \le 10^{18}$
- $1 \le k \le 20$
- $2 \le a_i \le n$


## Example


Input:


```
20 2
2 5
```


Output:


```
12
```


Explanation: the $12$ numbers are $2,4,5,6,8,10,12,14,15,16,18,20$.



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
 
ll const N = 1e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, k; cin>>n>>k;
  vi v(k); fir(k) cin>>v[i];

  ll res=0;
  fir(1LL<<k) if(i){
    ll pc=0, pr=1, po=0;
    fjr(k) if((i>>j)&1) pc++, po|=(pr>n/v[j]), pr*=v[j];

    if(po) continue;
    ll sg=((pc&1)? 1: -1);
    res+=sg*(n/pr);
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
