# Colored Chairs

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ chairs arranged in a circle. Each chair is either red or blue. The chairs are numbered $1, 2,\dots, n$; chairs $i$ and $i+1$ are next to each other for all $1 \le i \le n$. Here chair $n+1$ refers to chair $1$.


Your task is to find two chairs that have the same color and are next to each other.


To do this, you can ask questions: you can choose a chair and you will be told the color of that chair.


## Interaction


This is an interactive problem. Your code will interact with the grader using standard input and output. You should start by reading a single integer $n$: the number of chairs.


On your turn, you can print one of the following:


- "$?\ i$", where $1 \le i \le n$: ask the color of chair $i$. The grader will return R or B for red or blue.
- "$!\ i$": report that chairs $i$ and $i+1$ have the same color. Your program must terminate after this.


Each line should be followed by a line break. You must make sure the output gets flushed after printing each line.


## Constraints


- $3 \le n \le 2 \cdot 10^5$, $n$ is odd
- you can ask at most $20$ questions of type $?$


## Example

```
5
? 1
R
? 2
B
? 3
B
! 2
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
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
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

ll ask(ll i){
  cout<<"? "<<i<<en; cout.flush();
  char r; cin>>r;
  return r=='B';
}
void solve(){
  ll n; cin>>n;
  ll l=1, r=n;
  ll L=ask(l);
  if(L==ask(r)){
    cout<<"! "<<r<<en; cout.flush();
    return;
  }
  while(r>l){
    ll m = (l+r+1)/2;
    ll x = ask(m);
    ll y = (m&1)? (L==x): (L!=x);
    if(y) l=m;
    else r=m-1;
  }
  cout<<"! "<<l<<en; cout.flush();
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
