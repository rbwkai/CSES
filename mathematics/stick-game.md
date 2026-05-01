# Stick Game

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a game where two players remove sticks from a heap. The players move alternately, and the player who removes the last stick wins the game.


A set $P=\{p_1,p_2,\ldots,p_k\}$ determines the allowed moves. For example, if $P=\{1,3,4\}$, a player may remove $1$, $3$ or $4$ sticks.


Your task is find out for each number of sticks $1,2,\dots,n$ if the first player has a winning or losing position.


## Input


The first input line has two integers $n$ and $k$: the number of sticks and moves.


The next line has $k$ integers $p_1,p_2,\dots,p_k$ that describe the allowed moves. All integers are distinct, and one of them is $1$.


## Output


Print a string containing $n$ characters: W means a winning position, and L means a losing position.


## Constraints


- $1 \le n \le 10^6$
- $1 \le k \le 100$
- $1 \le p_i \le n$


## Example


Input:


```
10 3
1 3 4
```


Output:


```
WLWWWWLWLW
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


void solve(){
  ll n, k; cin>>n>>k;
  vi v(k); fir(k) cin>>v[i];

  vi dp(n+1, 0); 
  fir(n+1) fjr(k) if(i-v[j]>=0) dp[i]|=!dp[i-v[j]];

  fir(n) cout<<(dp[i+1]? "W": "L");
  cout<<en;
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
