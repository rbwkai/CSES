# Raab Game I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a two player game where each player has $n$ cards numbered $1,2,\dots,n$. On each turn both players place one of their cards on the table. The player who placed the higher card gets one point. If the cards are equal, neither player gets a point. The game continues until all cards have been played.


You are given the number of cards $n$ and the players' scores at the end of the game, $a$ and $b$. Your task is to give an example of how the game could have played out.


## Input


The first line contains one integer $t$: the number of tests.


Then there are $t$ lines, each with three integers $n$, $a$ and $b$.


## Output


For each test case print YES if there is a game with the given outcome and NO otherwise.


If the answer is YES, print an example of one possible game. Print two lines representing the order in which the players place their cards. You can give any valid example.


## Constraints


- $1 \le t \le 1000$
- $1 \le n \le 100$
- $0 \le a,b \le n$


## Example


Input:


```
5
4 1 2
2 0 1
3 0 0
2 1 1
4 4 1
```


Output:


```
YES
1 4 3 2
2 1 3 4
NO
YES
1 2 3
1 2 3
YES
1 2
2 1
NO
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
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
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
  ll a, b, n; cin>>n>>a>>b;
  vi v(n); fir(n) v[i]=i+1;

  if(a+b>n or (b==0 and a) or (b and a==0)) {cout<<"NO"<<en; return;}
  fir(a+b) v[i]=(i+b)%(a+b) +1;

  cout<<"YES"<<en;
  fir(n) cout<<v[i]<<ln;
  fir(n) cout<<i+1<<ln;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
