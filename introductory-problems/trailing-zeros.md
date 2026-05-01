# Trailing Zeros

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to calculate the number of trailing zeros in the factorial $n!$.


For example, $20!=2432902008176640000$ and it has $4$ trailing zeros.


## Input


The only input line has an integer $n$.


## Output


Print the number of trailing zeros in $n!$.


## Constraints


- $1 \le n \le 10^9$


## Example


Input:


```
20
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
  ll m=5, res=0;
  while(m<=n){
    res+=n/m;
    m*=5;
  }
  cout<<res<<endl;
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
