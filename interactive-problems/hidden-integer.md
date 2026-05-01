# Hidden Integer

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a hidden integer $x$. Your task is to find the value of $x$.


To do this, you can ask questions: you can choose an integer $y$ and you will be told if $y < x$.


## Interaction


This is an interactive problem. Your code will interact with the grader using standard input and output. You can start asking questions right away.


On your turn, you can print one of the following:


- "$?\ y$", where $1 \le y \le 10^9$: ask if $y < x$. The grader will return YES if $y < x$ and NO otherwise.
- "$!\ x$": report that the hidden integer is $x$. Your program must terminate after this.


Each line should be followed by a line break. You must make sure the output gets flushed after printing each line.


## Constraints


- $1 \le x \le 10^9$
- you can ask at most $30$ questions of type $?$


## Example

```
? 3
YES
? 6
YES
? 7
NO
! 7
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

bool ask(ll x){
  cout<<"? "<<x<<endl;
  string s; cin>>s;
  return s=="YES";
}
void ans(ll x){
  cout<<"! "<<x<<endl;
}

void solve(){
  ll l=1, r=1e9;
  while(l<r){
    ll m=(l+r)/2;
    if(ask(m)) l=m+1;
    else r=m;
  }
  ans(l);
}

int main(){
  //ios_base::sync_with_stdio(false);
  //cin.tie(0);
  
  int tt = 1; //cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
