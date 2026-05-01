# Removal Game

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a list of $n$ numbers and two players who move alternately. On each move, a player removes either the first or last number from the list, and their score increases by that number. Both players try to maximize their scores.


What is the maximum possible score for the first player when both players play optimally?


## Input


The first input line contains an integer $n$: the size of the list.


The next line has $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the list.


## Output


Print the maximum possible score for the first player.


## Constraints


- $1 \le n \le 5000$
- $-10^9 \le x_i \le 10^9$


## Example


Input:


```
4
4 5 1 3
```


Output:


```
8
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
  vi ps(n+1, 0); fir(n) ps[i+1]=ps[i]+v[i];

  grid dp(n, vi(n, -inf)); 
  function<ll(ll, ll)> rec = [&](ll l, ll r){
    if(l==r) return v[l];
    if(dp[l][r]+inf) return dp[l][r];

    return dp[l][r]=ps[r+1]-ps[l]-min(rec(l+1, r), rec(l, r-1));
  };
  cout<<rec(0, n-1)<<endl;
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
