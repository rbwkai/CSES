# Increasing Subsequence II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to calculate the number of increasing subsequences it contains. If two subsequences have the same values but in different positions in the array, they are counted separately.


## Input


The first input line has an integer $n$: the size of the array.


The second line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


## Output


Print one integer: the number of increasing subsequences modulo $10^9+7$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
3
2 1 3
```


Output:


```
5
```


Explanation: The increasing subsequences are $[2]$, $[1]$, $[3]$, $[2,3]$ and $[1,3]$.



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
using pii = pair<ll, ll>;
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
    for(++i; i<=ss; i+=i&-i) bit[i]= bit[i]+delta;
  }
  T query(int i){
    T res=0;
    for(++i; i>0; i-=i&-i) res= res+bit[i];
    return res;
  }
  long unsigned int size(){return ss;}
};

void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  ordered_set<ll> os; fir(n) os.insert(v[i]);
  fir(n) v[i] = os.order_of_key(v[i]);

  indexed_tree<mint> b(n);
  mint res=0;
  fir(n){
    mint c = b.query(v[i]-1) + 1;
    res=res+c; b.update(v[i], c);
  }
  cout<<res<<en;
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
