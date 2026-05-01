# Meet in the Middle

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ numbers. In how many ways can you choose a subset of the numbers with sum $x$?


## Input


The first input line has two numbers $n$ and $x$: the array size and the required sum.


The second line has $n$ integers $t_1,t_2,\dots,t_n$: the numbers in the array.


## Output


Print the number of ways you can create the sum $x$.


## Constraints


- $1 \le n \le 40$
- $1 \le x \le 10^9$
- $1 \le t_i \le 10^9$


## Example


Input:


```
4 5
1 2 3 2
```


Output:


```
3
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
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
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
    mint a=b, r=1;
    for( ; p; p>>=1, a=a*a) if(p&1) r=r*a;
    return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
};

void solve(){
  ll n, x; cin>>n>>x;
  vi v(n); fir(n) cin>>v[i];
  
  function<vi(ll, ll)> gss=[&](ll l, ll r){
    ll len = (r-l+1);

    vi rv;
    for(ll m=0; m<(1<<len); m++){
      ll sm=0; fir(len) sm+=v[l+i]*((m>>i)&1);
      rv.push_back(sm);
    }
    return rv;
  };

  vi lft = gss(0, n/2-1), rgt=gss(n/2, n-1); 
  sort(lft.begin(), lft.end());
  sort(rgt.begin(), rgt.end());

  ll res=0;
  for(ll i: lft){
    auto low = lower_bound(rgt.begin(), rgt.end(), x-i);
    auto hig = upper_bound(rgt.begin(), rgt.end(), x-i);
    res += hig - low;
  }
  cout<<res<<en;
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
