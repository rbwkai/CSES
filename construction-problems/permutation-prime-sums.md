# Permutation Prime Sums

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given $n$, create two permutations $a$ and $b$ of size $n$ such that $a_i+b_i$ is prime for $i=1,2,\dots,n$.


## Input


The only line has an integer $n$.


## Output


Print two permutations. You can print any valid solution. If there are no solutions, print IMPOSSIBLE.


## Constraints


- $1 \le n \le 10^5$


## Example


Input:


```
5
```


Output:


```
2 1 3 5 4
5 1 4 2 3
```


Explanation: The sums are $2+5=7$, $1+1=2$, $3+4=7$, $5+2=7$ and $4+3=7$ which all are primes.



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
ll const N = 2e6+6;
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

vi primes;
void seive(){
  vi prime(N+1, 0);
  for(int x=2; x<=N; ++x){
    if(prime[x]) continue;
    primes.pb(x);
    for(int u=2*x; u<=N; u+=x){
      prime[u]=x;
    }
  }
}
void solve(){
  ll n; cin>>n;
  vi b;

  auto rec=[&](ll x){
    ll id = upper_bound(all(primes), 2*x) -primes.begin()-1;
    ll p = primes[id];
    ll s = p - x;
    for(int i=x; i>=s; --i) b.pb(p-i);
    return s-1;
  };

  ll t = n;
  while(t) t=rec(t);
  fir(n) cout<<i+1<<ln;
  fir(n) cout<<b[ii]<<ln;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  seive();
  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
