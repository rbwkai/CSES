# Coin Combinations I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a money system consisting of $n$ coins. Each coin has a positive integer value. Your task is to calculate the number of distinct ways you can produce a money sum $x$ using the available coins.


For example, if the coins are $\{2,3,5\}$ and the desired sum is $9$, there are $8$ ways:


- $2+2+5$
- $2+5+2$
- $5+2+2$
- $3+3+3$
- $2+2+2+3$
- $2+2+3+2$
- $2+3+2+2$
- $3+2+2+2$


## Input


The first input line has two integers $n$ and $x$: the number of coins and the desired sum of money.


The second line has $n$ distinct integers $c_1,c_2,\dots,c_n$: the value of each coin.


## Output


Print one integer: the number of ways modulo $10^9+7$.


## Constraints


- $1 \le n \le 100$
- $1 \le x \le 10^6$
- $1 \le c_i \le 10^6$


## Example


Input:


```
3 9
2 3 5
```


Output:


```
8
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

const ll mod=1e9+7;

void solve(){
  ll n, x; cin>>n>>x;
  vi v(n); fir(n) cin>>v[i];

  vi dp(x+1, 0); dp[0]=1;
  fir(x+1) fjr(n){
    if(i-v[j]>=0) dp[i]+=dp[i-v[j]];
    dp[i]%=mod;
  }
  cout<<dp[x]<<endl;
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; // cin>>tC;
  while(tC--){
    solve();
  }
}
```
