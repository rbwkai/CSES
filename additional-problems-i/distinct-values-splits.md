# Distinct Values Splits

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers. Your task is to count the number of ways to split the array into continuous segments such that all segments consists of distinct values.


## Input


The first line has an integers $n$: the size of the array.


The next line has $n$ integers $x_1, x_2,\dots, x_n$: the contents of the array.


## Output


Print one integer: the answer to the problem modulo $10^9 + 7$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
4
1 2 1 3
```


Output:


```
6
```


Explanation: There are six valid splits:


- $[1], [2], [1], [3]$
- $[1], [2], [1, 3]$
- $[1], [2, 1], [3]$
- $[1], [2, 1, 3]$
- $[1, 2], [1], [3]$
- $[1, 2], [1, 3]$



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
#define F first
#define S second
#define pb push_back
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)



// 一心不乱
ll const N = 1e7;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9 + 7; //998244353;
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
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];
  map<ll, ll> mp;

  vector<mint> dp(n+1); dp[0] = 1;
  ll s = -1;
  fir(n){
    if(mp.count(v[i])) s=max(s, mp[v[i]]);
    mint r = dp[i]; if(s>=0) r = r-dp[s];
    dp[i+1] = dp[i]+r;
    mp[v[i]] = i;
  }
  cout<<dp[n]-dp[n-1]<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
