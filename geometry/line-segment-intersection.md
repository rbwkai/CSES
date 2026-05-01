# Line Segment Intersection

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are two line segments: the first goes through the points $(x_1,y_1)$ and $(x_2,y_2)$, and the second goes through the points $(x_3,y_3)$ and $(x_4,y_4)$.


Your task is to determine if the line segments intersect, i.e., they have at least one common point.


## Input


The first input line has an integer $t$: the number of tests.


After this, there are $t$ lines that describe the tests. Each line has eight integers $x_1$, $y_1$, $x_2$, $y_2$, $x_3$, $y_3$, $x_4$ and $y_4$.


## Output


For each test, print "YES" if the line segments intersect and "NO" otherwise.


## Constraints


- $1 \le t \le 10^5$
- $-10^9 \le x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4 \le 10^9$
- $(x_1,y_1) \neq (x_2,y_2)$
- $(x_3,y_3) \neq (x_4,y_4)$


## Example


Input:


```
5
1 1 5 3 1 2 4 3
1 1 5 3 1 1 4 3
1 1 5 3 2 3 4 1
1 1 5 3 2 4 4 1
1 1 5 3 3 2 7 4
```


Output:


```
NO
YES
YES
YES
YES
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
  ll a, b, c, d, p, q, r, s;
  cin>>a>>b>>c>>d>>p>>q>>r>>s;

  ll aa = area(a, b, c, d, p, q), bb = area(a, b, c, d, r, s);
  ll pp = area(a, b, p, q, r, s), qq = area(c, d, p, q, r, s);

  if(aa) aa/=abs(aa); if(bb) bb/=abs(bb);
  if(pp) pp/=abs(pp); if(qq) qq/=abs(qq);

  if(aa!=bb and pp!=qq) return cout<<"YES"<<en, void();
  if(!aa and !bb and !pp and !qq){
    if(a>c) swap(a, c); if(b>d) swap(b, d);
    if(p>r) swap(p, r); if(q>s) swap(q, s);
    cout<<(max(a, p)<=min(c, r) and max(b, q)<=min(d, s)? "YES": "NO")<<en;
    return;
  }
  cout<<"NO"<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt) solve();
}
```
