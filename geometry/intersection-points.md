# Intersection Points

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given $n$ horizontal and vertical line segments, your task is to calculate the number of their intersection points.


You can assume that no parallel line segments intersect, and no endpoint of a line segment is an intersection point.


## Input


The first line has an integer $n$: the number of line segments.


Then there are $n$ lines describing the line segments. Each line has four integers: $x_1$, $y_1$, $x_2$ and $y_2$: a line segment begins at point $(x_1,y_1)$ and ends at point $(x_2,y_2)$.


## Output


Print the number of intersection points.


## Constraints


- $1 \le n \le 10^5$
- $-10^6 \le x_1 \le x_2 \le 10^6$
- $-10^6 \le y_1 \le y_2 \le 10^6$
- $(x_1,y_1) \neq (x_2,y_2)$


## Example


Input:


```
3
2 3 7 3
3 1 3 5
6 2 6 6
```


Output:


```
2
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


void solve(){
  ll n; cin>>n;
  grid q;
  fir(n){
    ll a, b, c, d;
    cin>>a>>b>>c>>d;
    if(a==c){ //vertical
      q.push_back({a, 0, b, d});
    }
    if(b==d){ //horizontal
      q.push_back({a, +1, b});
      q.push_back({c, -1, b});
    }
  }

  sort(all(q));
  ordered_set<ll> os;
  ll res = 0;
  fir(sz(q)){
    if(!q[i][1]){
      ll s=q[i][2], e=q[i][3];
      ll si = os.order_of_key(s);
      ll ei = os.order_of_key(e);
      res += ei-si;
    }
    else{
      if(q[i][1]==1){
        os.insert(q[i][2]);
      }
      else{
        os.erase(os.find(q[i][2]));
      }
    }
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
