# String Matching

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a string and a pattern, your task is to count the number of positions where the pattern occurs in the string.


## Input


The first input line has a string of length $n$, and the second input line has a pattern of length $m$. Both of them consist of characters a–z.


## Output


Print one integer: the number of occurrences.


## Constraints


- $1 \le n,m \le 10^6$


## Example


Input:


```
saippuakauppias
pp
```


Output:


```
2
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
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 1e6+6;
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
    mint a=b, r=1; for( ; p; p>>=1, a=a*a) if(p&1) r=r*a; return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
}; 


void solve(){
  string s, p; cin>>s>>p;
  ll n=sz(s), m=sz(p);

  vi dp(m); //KMP
  ll len = 0;
  fir(m) if(i){
    while(len>0 and p[len]!=p[i])
      len = dp[len-1];
    len += (p[len]==p[i]);
    dp[i] = len;
  }

  ll i=0, j=0, r=0;
  while(i<n){
    if(s[i]==p[j]){
      i++, j++;
      if(j==m) j=dp[j-1], r++;
    }
    else{
      if(j) j=dp[j-1];
      else i++;
    }
  }
  cout<<r<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
