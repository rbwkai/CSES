# Sum of Divisors

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Let $\sigma(n)$ denote the sum of divisors of an integer $n$. For example, $\sigma(12)=1+2+3+4+6+12=28$.


Your task is to calculate the sum $\sum_{i=1}^n \sigma(i)$ modulo $10^9+7$.


## Input


The only input line has an integer $n$.


## Output


Print $\sum_{i=1}^n \sigma(i)$ modulo $10^9+7$.


## Constraints


- $1 \le n \le 10^{12}$


## Example


Input:


```
5
```


Output:


```
21
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
  ll n; cin>>n;
  ll res=0;

  for(ll d=1; d*d<=n; ++d){
    res=(res+d*(n/d))%mod;
    if(n/d>d){
      ll sv=n/d, ev=n/(d+1);
      ll sm=(sv+ev+1)%mod; ll rn=(sv-ev)%mod;
      sm=(sm*d)%mod; rn=(rn*500000004)%mod;
      ll del=(sm*rn)%mod;
      res=(res+del)%mod;
    }
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
