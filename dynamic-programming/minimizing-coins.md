# Minimizing Coins

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a money system consisting of $n$ coins. Each coin has a positive integer value. Your task is to produce a sum of money $x$ using the available coins in such a way that the number of coins is minimal.


For example, if the coins are $\{1,5,7\}$ and the desired sum is $11$, an optimal solution is $5+5+1$ which requires $3$ coins.


## Input


The first input line has two integers $n$ and $x$: the number of coins and the desired sum of money.


The second line has $n$ distinct integers $c_1,c_2,\dots,c_n$: the value of each coin.


## Output


Print one integer: the minimum number of coins. If it is not possible to produce the desired sum, print $-1$.


## Constraints


- $1 \le n \le 100$
- $1 \le x \le 10^6$
- $1 \le c_i \le 10^6$


## Example


Input:


```
3 11
1 5 7
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

ll mod=1e9+7;

void solve(){
  ll n, x; cin>>n>>x;
  vi v(n); fir(n) cin>>v[i];

  vi dp(x+1, INT_MAX); dp[0]=0;
  fir(x+1){
    for(ll c: v){
      if(i-c>=0) dp[i]=min(dp[i], dp[i-c]+1);
    }
  }
  cout<<((dp[x]<INT_MAX)? dp[x]: -1)<<endl;
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
