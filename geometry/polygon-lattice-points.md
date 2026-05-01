# Polygon Lattice Points

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a polygon, your task is to calculate the number of lattice points inside the polygon and on its boundary. A lattice point is a point whose coordinates are integers.


The polygon consists of $n$ vertices $(x_1,y_1),(x_2,y_2),\dots,(x_n,y_n)$. The vertices $(x_i,y_i)$ and $(x_{i+1},y_{i+1})$ are adjacent for $i=1,2,\dots,n-1$, and the vertices $(x_1,y_1)$ and $(x_n,y_n)$ are also adjacent.


## Input


The first input line has an integer $n$: the number of vertices.


After this, there are $n$ lines that describe the vertices. The $i$th such line has two integers $x_i$ and $y_i$.


You may assume that the polygon is simple, i.e., it does not intersect itself.


## Output


Print two integers: the number of lattice points inside the polygon and on its boundary.


## Constraints


- $3 \le n \le 10^5$
- $-10^9 \le x_i, y_i \le 10^9$


## Example


Input:


```
4
1 1
5 3
3 5
1 4
```


Output:


```
6 8
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
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
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


ll area(ll x1, ll y1, ll x2, ll y2, ll x3, ll y3){
  ll area = x1*y2 - x2*y1
          + x2*y3 - x3*y2
          + x3*y1 - x1*y3;
  return area;
}
void solve(){
  ll n; cin>>n;
  vi x(n), y(n);
  fir(n) cin>>x[i]>>y[i];

  ll A = 0;
  fir(n-2){
    A += area(x[0], y[0], x[i+1], y[i+1], x[i+2], y[i+2]);
  } 

  ll B = 0;
  fir(n){
    ll j = (i+1)%n;
    B += abs(__gcd(x[j]-x[i], y[j]-y[i]));
  }

  //pick's theorem
  ll I = (abs(A) - B + 2)/2;
  cout<<I<<" "<<B<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
