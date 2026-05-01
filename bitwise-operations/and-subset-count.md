# And Subset Count

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers. Your task is to calculate the number of non-empty subsets whose elements' bitwise and is equal to $k$ for each $k = 0, 1,\dots, n$.


## Input


The first line has an integer $n$: the size of the array.


The next line has $n$ integers $a_1, a_2,\dots, a_n$: the contents of the array.


## Output


Print $n + 1$ integers as specified above modulo $10^9 + 7$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $0 \le a_i \le n$


## Example


Input:


```
4
3 1 3 4
```


Output:


```
7 4 0 3 1
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
using pii = pair<ll, ll>;
using grid = vector<vi>;
 
template<class T>
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

struct mint{
  ll v; 
  mint(ll _v=0) {v = (_v%mod +mod)%mod;}

  friend mint operator+(const mint& a, const mint& b){ return mint(a.v + b.v); }
  friend mint operator-(const mint& a, const mint& b){ return mint(a.v - b.v); }
  friend mint operator*(const mint& a, const mint& b){ return mint(a.v * b.v); }
  friend mint operator/(const mint& a, const mint& b){ return a*minv(b); }
  friend mint mpow(const mint& b, ll p){
    mint a=b, r=1;
    for( ; p; p>>=1, a=a*a) if(p&1) r=r*a;
    return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
}; 


void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  ll logA = 20;
  vi sup(1LL<<logA); fir(n) sup[v[i]]++;
  fjr(logA) fir(1<<logA) if((i>>j)&1){
    sup[i^(1LL<<j)]+=sup[i];
  } 

  vector<mint> ssup(1LL<<logA);
  fir(1<<logA) ssup[i]=mpow(mint(2), sup[i])-1;
  fjr(logA) fir(1<<logA) if((i>>j)&1){
    ssup[i^(1LL<<j)] = ssup[i^(1LL<<j)] - ssup[i];
  } 

  fir(n+1) cout<<ssup[i]<<" ";
  cout<<en;
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
