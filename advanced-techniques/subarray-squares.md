# Subarray Squares

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ elements, your task is to divide into $k$ subarrays. The cost of each subarray is the square of the sum of the values in the subarray. What is the minimum total cost if you act optimally?


## Input


The first input line has two integers $n$ and $k$: the array elements and the number of subarrays. The array elements are numbered $1,2,\dots,n$.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


## Output


Print one integer: the minimum total cost.


## Constraints


- $1 \le k \le n \le 3000$
- $1 \le x_i \le 10^5$


## Example


Input:


```
8 3
2 3 1 2 2 3 4 1
```


Output:


```
110
```


Explanation: An optimal solution is $[2,3,1]$, $[2,2,3]$, $[4,1]$, whose cost is $(2+3+1)^2+(2+2+3)^2+(4+1)^2=110$.



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


void solve(){
  ll n, x; cin>>n>>x;
  vi v(n); fir(n) cin>>v[i];
  vi ps(n+1); fir(n) ps[i+1]=ps[i]+v[i];

  vi pdp(n+1, inf), ndp(n+1, inf); 
  pdp[0] = 0;
  fjr(x){
    deque<pi> dq;
    dq.push_back({-2*ps[j], pdp[j] + ps[j]*ps[j]});

    fir(n) if(i>=j){
      while(sz(dq) > 1){
        auto [m0, b0] = dq[0];
        auto [m1, b1] = dq[1];
        if(m0*ps[i+1] + b0 >= m1*ps[i+1] + b1) dq.pop_front();
        else break;
      }
      ndp[i+1] = ps[i+1]*ps[i+1] + dq.front().first*ps[i+1] + dq.front().second;

      pi nl = {-2*ps[i+1], pdp[i+1] + ps[i+1]*ps[i+1]};
      while (sz(dq) > 1) {
        auto [mx, bx] = dq[sz(dq)-2];
        auto [my, by] = dq[sz(dq)-1];
        auto [mz, bz] = nl;

        if ((bz-bx)*(mx-my) <= (by-bx)*(mx-mz))
          dq.pop_back();
        else
          break;
      }
      dq.push_back(nl);
    }

    swap(pdp, ndp);
    fill(ndp.begin(), ndp.end(), inf);
  }
  cout<<pdp[n]<<en;
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
