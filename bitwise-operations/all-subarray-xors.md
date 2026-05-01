# All Subarray Xors

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to find all integers that are the xor sum in some subarray.


## Input


The first line has an integer $n$: the size of the array.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


## Output


First print an integer $k$: the number of distinct integers that are the xor sum in some subarray.


After this print $k$ integers: the xor sums in increasing order.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $0 \le x_i \le 10^6$


## Example


Input:


```
4
5 1 5 9
```


Output:


```
7
1 4 5 8 9 12 13
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


vi fwht(vi& a, bool invert){
  ll n = sz(a);
  vi f(a);

  for(ll len=1; len<n; len<<=1){
    for(ll i=0; i<n; i+=2*len){
      fjr(len){
        ll u = f[i+j], v = f[i+j+len];
        f[i+j] = u+v;
        f[i+j+len] = u-v;
      }
    }
  }
  if(invert) for(ll& x: f) x/=n;
  return f;
}
void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  ll px=0;
  set<ll> unq; unq.insert(0);
  fir(n) px ^= v[i], unq.insert(px);

  ll M = (1<<20);
  vi a(M, 0); for(ll x: unq) a[x]=1;

  vi fwhtA = fwht(a, false);
  fir(M) fwhtA[i] *= fwhtA[i];
  vi A = fwht(fwhtA, true);

  ll nz = sz(unq)==n+1;
  vi res; fir(M) if(A[i]) res.push_back(i);
  cout<<sz(res)-nz<<en;
  for(ll x: res) if(!nz or x) cout<<x<<" ";
  cout<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
