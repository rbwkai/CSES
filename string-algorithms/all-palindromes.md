# All Palindromes

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a string, calculate for each position the length of the longest palindrome that ends at that position.


## Input


The only line contains a string of length $n$. Each character is one of a–z.


## Output


Print $n$ numbers: the length of each palindrome.


## Constraints


- $1 \le n \le 2 \cdot 10^5$


## Example


Input:


```
ababbababaa
```


Output:


```
1 1 3 3 2 4 6 8 5 5 2
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
  string s; cin>>s;
  string t="#"; fir(sz(s)) t+=s[i], t+='#';
  t = '@'+t+'$';

  ll n=sz(t);
  vi dp(n); //Manacher
  ll c = 0, r = -1;
  fir(n-1) if(i){
    ll m = 2*c - i;
    if(i<=r) dp[i] = min(r-i+1, dp[m]);
    while(t[i+1+dp[i]] == t[i-1-dp[i]]) dp[i]++;
    if(i+dp[i]-1 > r) c=i, r=i+dp[i]-1; 
  }

  vi res(sz(s));
  fir(n){
    ll l = (i-1-dp[i])/2;
    ll r = l+dp[i]-1;
    res[r] = max(res[r], r-l+1);
  }

  fir(sz(s)) if(i) res[ii]=max(res[ii], res[ii+1]-2);
  fir(sz(s)) cout<<res[i]<<" ";
  cout<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
