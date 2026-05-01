# SOS Bit Problem

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a list of $n$ integers, your task is to calculate for each element $x$:



the number of elements $y$ such that $x \mid y = x$
the number of elements $y$ such that $x \mathrel{\&} y = x$
the number of elements $y$ such that $x \mathrel{\&} y \neq 0$

## Input


The first line has an integer $n$: the size of the list.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the elements of the list.


## Output


Print $n$ lines: for each element the required values.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^6$


## Example


Input:


```
5
3 7 2 9 2
```


Output:


```
3 2 5
4 1 5
2 4 4
1 1 3
2 4 4
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
using pii = pair<ll, ll>;
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


void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  ll logA = 20;
  vi sub(1LL<<logA), sup(1LL<<logA); fir(n) sub[v[i]]++, sup[v[i]]++;
  fjr(logA) fir(1<<logA) if((i>>j)&1){
    sub[i]+=sub[i^(1LL<<j)];
    sup[i^(1LL<<j)]+=sup[i];
  } 

  fir(n) cout<<sub[v[i]]<<" "
             <<sup[v[i]]<<" "
             <<n-sub[((1LL<<logA)-1)^v[i]]<<en;
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
