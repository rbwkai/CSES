# K-th Highest Score

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There were $n$ coders from Finland and $n$ coders from Sweden in a programming contest. It turned out that after the contest, each coder had a distinct score.


Your task is to find the $k$-th highest score in the contest.


To do this, you can ask questions: you can choose a country (Finland or Sweden) and an integer $i$ and you will be told the $i$-th highest score for the chosen country.


## Interaction


This is an interactive problem. Your code will interact with the grader using standard input and output. You should start by reading two integers $n$ and $k$.


On your turn, you can print one of the following:


- "$\mathrm{F}\ i$", where $1 \le i \le n$: ask the $i$-th highest score for Finland.
- "$\mathrm{S}\ i$", where $1 \le i \le n$: ask the $i$-th highest score for Sweden.
- "$!\ s$": report that the $k$-th highest score is $s$. Your program must terminate after this.


Each line should be followed by a line break. You must make sure the output gets flushed after printing each line.


## Constraints


- $1 \le n \le 10^5$
- $1 \le k \le 2n$
- each score is between $1$ and $10^9$
- you can ask at most $100$ queries of the first two types in total


## Example

```
3 1
F 1
9
S 1
8
! 9
```


Explanation: The scores for Finland are $[9, 4, 3]$ and the scores for Sweden are $[8, 6, 1]$. Since $k = 1$, the task is to find the highest score overall, which in this case is $9$.



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


ll ask(ll i, ll j, ll n){
  if(j<1) return inf;
  if(j>n) return -inf;

  cout<<(i? "S": "F")<<" "<<j<<endl;
  ll r; cin>>r;
  return r;
}
void ans(ll x){
  cout<<"! ";
  cout<<x<<endl;
}

void solve(){
  ll n, k; cin>>n>>k;
  
  ll l=0, r=n;
  while(l<=r){
    ll m = (l+r)/2;

    ll a=ask(0, m, n), aa=ask(0, m+1, n);
    ll b=ask(1, k-m, n), bb=ask(1, k-m+1, n);

    if(b>aa and a>bb) {ans(min(a, b)); return;}
    if(aa>b) l=m+1;
    if(bb>a) r=m;
  }
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
