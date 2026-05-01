# Permutation Rounds

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a sorted array $[1,2,\dots,n]$ and a permutation $p_1,p_2,\dots,p_n$. On each round, all elements move according to the permutation: the element at position $i$ moves to position $p_i$.


After how many rounds is the array sorted again for the first time?


## Input


The first line has an integer $n$.


The next line contains $n$ integers $p_1,p_2,\dots,p_n$.


## Output


Print the number of rounds modulo $10^9+7$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$


## Example


Input:


```
8
5 3 2 6 4 1 8 7
```


Output:


```
4
```


Explanation: The array changes as follows after the rounds:


- Round 1: $[6,3,2,5,1,4,8,7]$
- Round 2: $[4,2,3,1,6,5,7,8]$
- Round 3: $[5,3,2,6,4,1,8,7]$
- Round 4: $[1,2,3,4,5,6,7,8]$



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

vi lpf(N+1);
void pre(){
  for(int i=2; i<N; ++i){
    if(!lpf[i]) for(int j=i; j<=N; j+=i){
      if(!lpf[j]) lpf[j]=i;
    }
  }
}

void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i], v[i]--;

  map<ll, ll> mp;
  fir(n) if(v[i]+1){
    ll nx=v[i], sz=1, tm;
    v[i]=-1;
    while(v[nx]+1) tm=nx, sz++, nx=v[nx], v[tm]=-1; 

    while(sz>1){
      ll p=lpf[sz], e=0;
      while(sz%p == 0) sz/=p, e++;
      mp[p] = max(mp[p], e);
    }
  }

  mint res=1;
  for(auto [p, e]: mp) res = res*mpow(mint(p), e);
  cout<<res<<en;
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
