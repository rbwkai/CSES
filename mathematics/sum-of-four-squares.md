# Sum of Four Squares

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A well known result in number theory is that every non-negative integer can be represented as the sum of four squares of non-negative integers.


You are given a non-negative integer $n$. Your task is to find four non-negative integers $a$, $b$, $c$ and $d$ such that $n = a^2 + b^2 + c^2 + d^2$.


## Input


The first line has an integer $t$: the number of test cases.


Each of the next $t$ lines has an integer $n$.


## Output


For each test case, print four non-negative integers $a$, $b$, $c$ and $d$ that satisfy $n = a^2 + b^2 + c^2 + d^2$.


## Constraints


- $1 \le t \le 1000$
- $0 \le n \le 10^7$
- the sum of all $n$ is at most $10^7$


## Example


Input:


```
3
5
30
322266
```


Output:


```
2 1 0 0
1 2 3 4
314 159 265 358
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
#define F first
#define S second
#define pb push_back
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)



// 一心不乱
ll const N = 1e7;
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


gp_hash_table<ll, pi> mp;
vector<bool> ok(N+7);
void pre(){
  for(int a=0; a*a<=N; ++a){
    for(int b=0; b*b<=N - a*a; ++b){
      mp[a*a + b*b] = {a, b};
      ok[a*a + b*b] = true;
    }
  }
}
void solve(){
  ll n; cin>>n;
  for(int x=0; x<=n/2; x++){
    if(ok[x] and ok[n-x]){
      cout<<mp[x].F<<" "
          <<mp[x].S<<" "
          <<mp[n-x].F<<" "
          <<mp[n-x].S<<en;
      return;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  pre();

  int tt = 1; cin>>tt;
  fir(tt) solve();
}
```
