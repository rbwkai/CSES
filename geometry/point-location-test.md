# Point Location Test

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a line that goes through the points $p_1=(x_1,y_1)$ and $p_2=(x_2,y_2)$. There is also a point $p_3=(x_3,y_3)$.


Your task is to determine whether $p_3$ is located on the left or right side of the line or if it touches the line when we are looking from $p_1$ to $p_2$.


## Input


The first input line has an integer $t$: the number of tests.


After this, there are $t$ lines that describe the tests. Each line has six integers: $x_1$, $y_1$, $x_2$, $y_2$, $x_3$ and $y_3$.


## Output


For each test, print "LEFT", "RIGHT" or "TOUCH".


## Constraints


- $1 \le t \le 10^5$
- $-10^9 \le x_1, y_1, x_2, y_2, x_3, y_3 \le 10^9$
- $x_1 \neq x_2$ or $y_1 \neq y_2$


## Example


Input:


```
3
1 1 5 3 2 3
1 1 5 3 4 1
1 1 5 3 3 2
```


Output:


```
LEFT
RIGHT
TOUCH
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
  ll x1, y1, x2, y2, x3, y3;
  cin>>x1>>y1>>x2>>y2>>x3>>y3;

  ll area = x1*y2 - x2*y1
          + x2*y3 - x3*y2
          + x3*y1 - x1*y3;
  if(area==0) cout<<"TOUCH"<<en;
  if(area >0) cout<<"LEFT"<<en;
  if(area <0) cout<<"RIGHT"<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt) solve();
}
```
