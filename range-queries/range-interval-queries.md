# Range Interval Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array $x$ of $n$ integers, your task is to process $q$ queries of the form: how many integers $i$ satisfy $a \le i \le b$ and $c \le x_i \le d$?


## Input


The first line has two integers $n$ and $q$: the number of values and queries.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the array values.


Finally, there are $q$ lines describing the queries. Each line has four integers $a$, $b$, $c$ and $d$: how many integers $i$ satisfy $a \le i \le b$ and $c \le x_i \le d$?


## Output


Print the result of each query.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$
- $1 \le a \le b \le n$
- $1 \le c \le d \le 10^9$


## Example


Input:


```
8 4
3 2 4 5 1 1 5 3
2 4 2 4
5 6 2 9
1 8 1 5
3 3 4 4
```


Output:


```
2
0
8
1
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


template <class T> struct indexed_tree{
  int ss;
  vector<T> bit;

  indexed_tree(int n): ss(n), bit(n+1, 0) {}

  void update(int i, T delta){
    for(++i; i<=ss; i+=i&-i) bit[i]+=delta;
  }
  T query(int i){
    T res=0;
    for(++i; i>0; i-=i&-i) res+=bit[i];
    return res;
  }
  long unsigned int size(){return ss;}
};

void solve(){
  ll n, q; cin>>n>>q;

  vector<pi> vl(n);
  fir(n){
    ll x; cin>>x;
    vl[i] = {x, i};
  } sort(vl.begin(), vl.end());

  vector<tuple<ll, ll, ll, ll, ll>> qr(2*q);
  fir(q){
    ll a, b, c, d; cin>>a>>b>>c>>d;
    // query = {value, sign, left, right, id}
    qr[2*i] = {c-1, -1, a-1, b-1, i};
    qr[2*i+1] = {d, +1, a-1, b-1, i};
  } sort(qr.begin(), qr.end());

  vi res(q); 
  indexed_tree<ll> bt(n);
  ll vp=0;
  fir(2*q){
    auto [val, sgn, lft, rgt, idx] = qr[i];
    while(vp<n and vl[vp].first<=val){
      bt.update(vl[vp++].second, 1);
    }

    ll qq = bt.query(rgt)-bt.query(lft-1);
    res[idx] += qq * sgn;
  }

  fir(q) cout<<res[i]<<en;
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
