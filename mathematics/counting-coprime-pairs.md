# Counting Coprime Pairs

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a list of $n$ positive integers, your task is to count the number of pairs of integers that are coprime (i.e., their greatest common divisor is one).


## Input


The first input line has an integer $n$: the number of elements.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the list.


## Output


Print one integer: the answer for the task.


## Constraints


- $1 \le n \le 10^5$
- $1 \le x_i \le 10^6$


## Example


Input:


```
8
5 4 20 1 16 17 5 15
```


Output:


```
19
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
vi lpf(N+1), mob(N+1);
void pre(){
  inv[0]=0; fac[0]=ifc[0]=1;
  
  fir(N) if(i){
    inv[i] = (i==1? 1: (inv[i-mod%i]*(mod/i+1))%mod);
    fac[i] = (fac[i-1]*i)%mod;
    ifc[i] = (ifc[i-1]*inv[i])%mod;
  }
  
  for(int i=2; i<N; ++i){
    if(!lpf[i]) for(int j=i; j<=N; j+=i){
      if(!lpf[j]) lpf[j]=i;
    }
  }

  mob[1]=1;
  for(int i=2; i<N; i++){
    if(lpf[i/lpf[i]]==lpf[i]) mob[i]=0;
    else mob[i]=-1*mob[i/lpf[i]];
  }
}
 
void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];
  vi cnt(N+1); 
  fir(n) cnt[v[i]]++;

  ll res=0;
  fir(N) if(i and mob[i]){
    ll d=0;
    for(int j=i; j<N; j+=i) d+=cnt[j];
    res+=mob[i]*(d*(d-1))/2;
  }
  cout<<res<<en;
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
