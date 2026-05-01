# Fibonacci Numbers

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

The Fibonacci numbers can be defined as follows:


- $F_0=0$
- $F_1=1$
- $F_n = F_{n-2}+F_{n-1}$


Your task is to calculate the value of $F_n$ for a given $n$.


## Input


The only input line has an integer $n$.


## Output


Print the value of $F_n$ modulo $10^9+7$.


## Constraints


- $0 \le n \le 10^{18}$


## Example


Input:


```
10
```


Output:


```
55
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
 
ll const N = 2e6+6;
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
ll bx(ll a, ll b){
  ll res=1;
  while(b){
    if(b&1) res=(res*a)%mod;
    a=(a*a)%mod;
    b>>=1;
  }
  return res;
}

void solve(){
  ll n; cin>>n;

  grid m = {{0, 1},
            {1, 1}};
  function<void()> mul=[&](){
    grid nm={{0, 0}, {0, 0}};
    fir(2) fjr(2) for(int k=0; k<2; ++k) nm[i][j]=(nm[i][j]+m[i][k]*m[k][j])%mod;
    swap(m, nm);
  };

  vi v={0, 1};
  while(n){
    if(n&1){
      vi nv(2, 0);
      fir(2) fjr(2) nv[i]=(nv[i]+m[i][j]*v[j])%mod;
      swap(v, nv);
    }
    n>>=1;
    mul();
  }
  cout<<v[0]<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  pre();
  int tt = 1; //cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
