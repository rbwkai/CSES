# Permutation Order

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Let $p(n,k)$ denote the $k$th permutation (in lexicographical order) of $1 \dots n$. For example, $p(4,1)=[1,2,3,4]$ and $p(4,2)=[1,2,4,3]$.


Your task is to process two types of tests:



Given $n$ and $k$, find $p(n,k)$
Given $n$ and $p(n,k)$, find $k$

## Input


The first line has an integer $t$: the number of tests.


Each test is either "1 $n$ $k$" or "2 $n$ $p(n,k)$".


## Output


For each test, print the answer according to the example.


## Constraints


- $1 \le t \le 1000$
- $1 \le n \le 20$
- $1 \le k \le n!$


## Example


Input:


```
6
1 4 1
1 4 2
2 4 1 2 3 4
2 4 1 2 4 3
1 5 42
2 5 2 4 5 3 1
```


Output:


```
1 2 3 4
1 2 4 3
1
2
2 4 5 3 1
42
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

vi fac(21);
void solve(){
  ll t; cin>>t;

  if(t==1){
    ll n, k; cin>>n>>k; k--;
    vi p(n);
    ordered_set<ll> os; fir(n) os.insert(i+1);
    fir(n){
      ll cv = k/fac[ii]; 
      p[i] = *os.find_by_order(cv); k-=cv*fac[ii];
      os.erase(os.find(p[i]));
    }
    fir(n) cout<<p[i]<<ln;
  }
  if(t==2){
    ll n; cin>>n;
    vi v(n); fir(n) cin>>v[i];
    ll rk=1;
    ordered_set<ll> os; fir(n) os.insert(i+1);
    fir(n){
      ll mp = os.order_of_key(v[i]);
      rk += mp*fac[ii];
      os.erase(os.find(v[i]));
    }
    cout<<rk<<en;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  fac[0]=1;
  fir(20) fac[i+1]=fac[i]*(i+1);
  
  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
