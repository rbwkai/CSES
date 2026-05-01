# Corner Subgrid Count

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an $n \times n$ grid whose each square is either black or white. A subgrid is called beautiful if its height and width is at least two and all of its corners are black. How many beautiful subgrids are there within the given grid?


## Input


The first input line has an integer $n$: the size of the grid.


Then there are $n$ lines describing the grid: 1 means that a square is black and 0 means it is white.


## Output


Print the number of beautiful subgrids.


## Constraints


- $1 \le n \le 3000$


## Example


Input:


```
5
00010
11111
00110
11001
00010
```


Output:


```
4
```


---

## Solution

```cpp
//#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("popcnt")
 
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
  ll n; cin>>n;
  bitset<3003> v[3003];
  fir(n) cin>>v[i];

  ll res=0;
  fir(n) fjr(n) if(j>i){
    ll pc = (v[i]&v[j]).count();
    res+=pc*(pc-1);
  }
  cout<<res/2<<en;
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
