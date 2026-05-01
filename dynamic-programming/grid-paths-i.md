# Grid Paths I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider an $n \times n$ grid whose squares may have traps. It is not allowed to move to a square with a trap.


Your task is to calculate the number of paths from the upper-left square to the lower-right square. You can only move right or down.


## Input


The first input line has an integer $n$: the size of the grid.


After this, there are $n$ lines that describe the grid. Each line has $n$ characters: . denotes an empty cell, and * denotes a trap.


## Output


Print the number of paths modulo $10^9+7$.


## Constraints


- $1 \le n \le 1000$


## Example


Input:


```
4
....
.*..
...*
*...
```


Output:


```
3
```


---

## Solution

```cpp
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using vi = vector<ll>;
using pii = pair<ll, ll>;
using grid = vector<vi>;

#define fix(_oO) cout<<setprecision(_oO)<<fixed
#define fir(_oO) for(int i=0; i<_oO; ++i)
#define fjr(_oO) for(int j=0; j<_oO; ++j)
const ll mod = 1e9+7;

void solve(){
  ll n; cin>>n;
  grid in(n, vi(n, 0)), dp(n, vi(n, -1));
  dp[n-1][n-1]=1;

  fir(n) fjr(n){
    char c; cin>>c;
    in[i][j]=(c=='*');
  }
  
  function<ll(ll, ll)> rec = [&](ll r, ll c){
    if(in[r][c]) return dp[r][c]=0;
    if(dp[r][c]+1) return dp[r][c];
    
    dp[r][c]=0;
    if(r!=n-1) dp[r][c]+=rec(r+1, c);
    if(c!=n-1) dp[r][c]+=rec(r, c+1);
    return dp[r][c]%=mod;
  };
  cout<<rec(0, 0)<<endl;
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; //cin>>tC;
  while(tC--){
    solve();
  }
}
```
