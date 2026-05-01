# Number of Subset Xors

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to find the number of different subset xors.


## Input


The first line has an integer $n$: the size of the array.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


## Output


Print one integer: the number of different subset xors.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $0 \le x_i \le 10^9$


## Example


Input:


```
3
3 6 5
```


Output:


```
4
```


Explanation: The following values can be the xor of a subset:


- $0 = \text{xor of the empty set}$
- $3 = 3$
- $5 = 3 \oplus 6$
- $6 = 3 \oplus 5$


In this case, no other values can be the xor of a subset.



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

struct XorBase {
  ll logA, dim;
  vi basis;

  XorBase(): logA(64), dim(0), basis(logA) {}

  void insert(ll x){
    fir(logA) if((x>>ii)&1) {
      if(!basis[ii]) {basis[ii]=x, dim++; return;}
      x ^= basis[ii];
    }
  }
};

void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  XorBase xb; fir(n) xb.insert(v[i]);

  cout<<(1LL<<xb.dim)<<en;
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
