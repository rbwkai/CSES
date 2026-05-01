# Binomial Coefficients

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to calculate $n$ binomial coefficients modulo $10^9+7$.


A binomial coefficient ${a \choose b}$ can be calculated using the formula $\frac{a!}{b!(a-b)!}$. We assume that $a$ and $b$ are integers and $0 \le b \le a$.


## Input


The first input line contains an integer $n$: the number of calculations.


After this, there are $n$ lines, each of which contains two integers $a$ and $b$.


## Output


Print each binomial coefficient modulo $10^9+7$.


## Constraints


- $1 \le n \le 10^5$
- $0 \le b \le a \le 10^6$


## Example


Input:


```
3
5 3
8 1
9 5
```


Output:


```
10
8
126
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
 
ll const N = 1e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

vi inv(N+1), fac(N+1), ifc(N+1);
void pre(){
  inv[0]=0; fac[0]=ifc[0]=1;
  
  fir(N) if(i){
    inv[i] = (i==1? 1: (inv[i-mod%i]*(mod/i+1))%mod);
    fac[i] = (fac[i-1]*i)%mod;
    ifc[i] = (ifc[i-1]*inv[i])%mod;
  }
}

void solve(){
  ll a, b; cin>>a>>b;
  ll dnm = (ifc[b]*ifc[a-b])%mod;
  cout<<(fac[a]*dnm)%mod<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  pre();
  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
