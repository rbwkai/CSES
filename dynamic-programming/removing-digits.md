# Removing Digits

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an integer $n$. On each step, you may subtract one of the digits from the number.


How many steps are required to make the number equal to $0$?


## Input


The only input line has an integer $n$.


## Output


Print one integer: the minimum number of steps.


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
27
```


Output:


```
5
```


Explanation: An optimal solution is $27 \rightarrow 20 \rightarrow 18 \rightarrow 10 \rightarrow 9 \rightarrow 0$.



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
  vi dp(n+1, INT_MAX); dp[0]=0;

  fir(n+1){
    vi dg; ll t=i;
    while(t) {dg.push_back(t%10); t/=10;}

    for(ll d: dg) if(i-d>=0) dp[i]=min(dp[i], dp[i-d]+1);
  }
  cout<<dp[n]<<endl;
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
