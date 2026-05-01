# Monster Game I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are playing a game that consists of $n$ levels. Each level has a monster. On levels $1,2,\dots,n-1$, you can either kill or escape the monster. However, on level $n$ you must kill the final monster to win the game.


Killing a monster takes $sf$ time where $s$ is the monster's strength and $f$ is your skill factor (lower skill factor is better). After killing a monster, you get a new skill factor. What is the minimum total time in which you can win the game?


## Input


The first input line has two integers $n$ and $x$: the number of levels and your initial skill factor.


The second line has $n$ integers $s_1,s_2,\dots,s_n$: each monster's strength.


The third line has $n$ integers $f_1,f_2,\dots,f_n$: your new skill factor after killing a monster.


## Output


Print one integer: the minimum total time to win the game.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x \le 10^6$
- $1 \le s_1 \le s_2 \le \dots \le s_n \le 10^6$
- $x \ge f_1 \ge f_2 \ge \dots \ge f_n \ge 1$


## Example


Input:


```
5 100
20 30 30 50 90
90 60 20 20 10
```


Output:


```
4800
```


Explanation: The best way to play is to kill the third and fifth monster.



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
  vi s(n); fir(n) cin>>s[i];
  vi f(n); fir(n) cin>>f[i];

  vi dp(n); 
  deque<pi> dq; dq.push_back({x, 0});
  fir(n){
    while(sz(dq) > 1){
      auto [m0, b0] = dq[0];
      auto [m1, b1] = dq[1];

      if(m0*s[i] + b0 >= m1*s[i] + b1) dq.pop_front();
      else break;
    }
    dp[i] = dq[0].first*s[i] + dq[0].second;

    while(sz(dq) > 1){
      auto [mx, bx] = dq[sz(dq)-2];
      auto [my, by] = dq[sz(dq)-1];
      ll mz = f[i], bz = dp[i];

      if((bz-bx)*(mx-my) <= (by-bx)*(mx-mz)) dq.pop_back();
      else break;
    }
    dq.push_back({f[i], dp[i]});
  }
  cout<<dp[n-1]<<en;
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
