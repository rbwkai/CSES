# Bracket Sequences II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to calculate the number of valid bracket sequences of length $n$ when a prefix of the sequence is given.


## Input


The first input line has an integer $n$.


The second line has a string of $k$ characters: the prefix of the sequence.


## Output


Print the number of sequences modulo $10^9+7$.


## Constraints


- $1 \le k \le n \le 10^6$


## Example


Input:


```
6
(()
```


Output:


```
2
```


Explanation: There are two possible sequences: (())() and (()()).



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
ll const inf = 0x3f3f3f3f3f3f;
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

vector<mint> inv(N+1), fac(N+1), ifc(N+1);
void pre(){
  inv[0]=0; fac[0]=ifc[0]=1;
  
  fir(N) if(i){
    inv[i] = i==1? 1: (inv[i-mod%i]*(mod/i+1));
    fac[i] = (fac[i-1]*i);
    ifc[i] = (ifc[i-1]*inv[i]);
  }
}
mint nCr(ll n, ll r){
  if(r>n or r<0) return 0;
  return fac[n]/(fac[r]*fac[n-r]);
}
mint ways(ll x, ll y){
  if((x+y)&1) return 0;
  if(abs(y)>x) return 0;

  ll g = (x+y)/2;
  mint res = nCr(x, g);
  return res;
}

void solve(){
  ll n; cin>>n;
  string s; cin>>s;

  ll f=1, p=0; fir(sz(s)) p+=(s[i]=='('? -1: 1), f&=(p<=0);
  n-=sz(s);

  cout<<f*(ways(n, p) - ways(n, -2+p))<<en;
}


int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  pre();
  int tt = 1; //cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
