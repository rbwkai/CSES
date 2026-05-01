# Exponentiation

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to efficiently calculate values $a^b$ modulo $10^9+7$.


Note that in this task we assume that $0^0=1$.


## Input


The first input line contains an integer $n$: the number of calculations.


After this, there are $n$ lines, each containing two integers $a$ and $b$.


## Output


Print each value $a^b$ modulo $10^9+7$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $0 \le a,b \le 10^9$


## Example


Input:


```
3
3 4
2 8
123 123
```


Output:


```
81
256
921450052
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
  ll a, b; cin>>a>>b;
  ll res=1;
  while(b){
    if(b&1) res=(res*a)%mod;
    a=(a*a)%mod;
    b>>=1;
  }
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
