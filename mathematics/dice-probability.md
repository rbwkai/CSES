# Dice Probability

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You throw a dice $n$ times, and every throw produces an outcome between $1$ and $6$. What is the probability that the sum of outcomes is between $a$ and $b$?


## Input


The only input line contains three integers $n$, $a$ and $b$.


## Output


Print the probability rounded to six decimal places (rounding half to even).


## Constraints


- $1 \le n \le 100$
- $1 \le a \le b \le 6n$


## Example


Input:


```
2 9 10
```


Output:


```
0.194444
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
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, a, b; cin>>n>>a>>b;
  vector<vector<double>> dp(n+1, vector<double>(6*n+1, 0)); 
  fir(6*n+1) dp[0][i]=1;

  fir(n) fjr(6*n) for(int m=1; m<=min(6, j+1); m++){
    dp[i+1][j+1]+=dp[i][j+1-m]/6;
  }
  fix(6);
  cout<<dp[n][b]-dp[n][a-1]<<en;
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
