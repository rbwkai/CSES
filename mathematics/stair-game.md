# Stair Game

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a staircase consisting of $n$ stairs, numbered $1,2,\ldots,n$. Initially, each stair has some number of balls.


There are two players who move alternately. On each move, a player chooses a stair $k$ where $k \neq 1$ and it has at least one ball. Then, the player moves any number of balls from stair $k$ to stair $k-1$. The player who moves last wins the game.


Your task is to find out who wins the game when both players play optimally.


Note that if there are no possible moves at all, the second player wins.


## Input


The first input line has an integer $t$: the number of tests. After this, $t$ test cases are described:


The first line contains an integer $n$: the number of stairs.


The next line has $n$ integers $p_1,p_2,\ldots,p_n$: the initial number of balls on each stair.


## Output


For each test, print "first" if the first player wins the game and "second" if the second player wins the game.


## Constraints


- $1 \le t \le 2 \cdot 10^5$
- $1 \le n \le 2 \cdot 10^5$
- $0 \le p_i \le 10^9$
- the sum of all $n$ is at most $2 \cdot 10^5$


## Example


Input:


```
3
3
0 2 1
4
1 1 1 1
2
5 3
```


Output:


```
first
second
first
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
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

vi inv(N+1), fac(N+1), ifc(N+1);
void pre(){
  inv[0]=0; fac[0]=ifc[0]=1;
  
  fir(N) if(i){
    inv[i] = (i==1? 1: (inv[i-mod%i]*(mod/i+1))%mod);
    fac[i] = (fac[i-1]*i)%mod;
    ifc[i] = (ifc[i-1]*inv[i])%mod;
  }
}
ll bx(ll a, ll b){
  ll res=1;
  while(b){
    if(b&1) res=(res*a)%mod;
    a=(a*a)%mod;
    b>>=1;
  }
  return res;
}

grid mm(grid& a, grid& b){
  ll n=sz(a), c=sz(a[0]), m=sz(b[0]);
  grid res(n, vi(m, 0));

  fir(n) fjr(m) for(int k=0; k<c; ++k){
    res[i][j]+=a[i][k]*b[k][j];
    res[i][j]%=mod;
  }
  return res;
}

void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  ll t=0;
  fir(n) if(i&1) t^=v[i];

  cout<<(t? "first": "second")<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  pre();
  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
