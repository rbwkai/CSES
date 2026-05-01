# Bit Strings

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to calculate the number of bit strings of length $n$.


For example, if $n=3$, the correct answer is $8$, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.


## Input


The only input line has an integer $n$.


## Output


Print the result modulo $10^9+7$.


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
3
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

ll mod=1e9+7;

void solve(){
  ll n; cin>>n;
  ll res=1;
  while(n--){
    res=(res*2)%mod;
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
