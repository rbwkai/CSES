# Knuth Division

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ numbers, your task is to divide it into $n$ subarrays, each of which has a single element.


On each move, you may choose any subarray and split it into two subarrays. The cost of such a move is the sum of values in the chosen subarray.


What is the minimum total cost if you act optimally?


## Input


The first input line has an integer $n$: the array size. The array elements are numbered $1,2,\dots,n$.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


## Output


Print one integer: the minimum total cost.


## Constraints


- $1 \le n \le 5000$
- $1 \le x_i \le 10^9$


## Example


Input:


```
5
2 7 3 2 5
```


Output:


```
43
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
  vi v(n); fir(n) cin>>v[i];
  vi ps(n+1, 0); fir(n) ps[i+1]=ps[i]+v[i];

  grid opt(n, vi(n, -1)), dp(n, vi(n, inf));
  fir(n) opt[i][i]=i;
  fir(n) dp[i][i]=0;

  fjr(n) for(int i=j-1; i>=0; i--){
    ll mn=inf, cst=ps[j+1]-ps[i];
    for(int k=opt[i][j-1]; k<=min((ll)j-1, opt[i+1][j]); ++k){
      if(mn>=dp[i][k]+dp[k+1][j]+cst){
        opt[i][j]=k;
        mn=dp[i][k]+dp[k+1][j]+cst;
      }
    }
    dp[i][j]=mn;
  } 
  cout<<dp[0][n-1]<<en;
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
