# Distinct Values Sum

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array $x_1,x_2,\dots,x_n$. Let $d(a,b)$ denote the number of distinct values in the subarray $x_a,x_{a+1},\dots,x_b$.


Your task is to calculate the sum $\sum_{a=1}^n \sum_{b=a}^n d(a,b)$, i.e., the sum of $d(a,b)$ for all subarrays.


## Input


The first line has an integer $n$: the array size.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the array contents.


## Output


Print one integer: the required sum.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
5
1 2 3 1 1
```


Output:


```
29
```


Explanation: In this array, $6$ subarrays have $1$ distinct value, $4$ subarrays have $2$ distinct values and $5$ subarrays have $3$ distinct values. Thus, the sum is $6\cdot1+4\cdot2+5\cdot3=29$.



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
ll const mod = 998244353;
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

  ll res=0;
  fir(n){
    ll start = -1; if(mp.count(v[i])) start=mp[v[i]];
    res += (n-i)*(i-start);
    mp[v[i]] = i;
  }
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
