# Dice Combinations

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to count the number of ways to construct sum $n$ by throwing a dice one or more times. Each throw produces an outcome between $1$ and  $6$.


For example, if $n=3$, there are $4$ ways:


- $1+1+1$
- $1+2$
- $2+1$
- $3$


## Input


The only input line has an integer $n$.


## Output


Print the number of ways modulo $10^9+7$.


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
3
```


Output:


```
4
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
  ll n; cin>>n;
  vi v(n+1, 0); v[0]=1;
  fir(n+1) fjr(6){
    if(i-j-1>=0) v[i]=(v[i]+v[i-j-1])%mod;
  }
  cout<<v[n]<<endl;
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
