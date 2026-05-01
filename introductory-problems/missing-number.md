# Missing Number

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given all numbers between $1,2,\ldots,n$ except one. Your task is to find the missing number.


## Input


The first input line contains an integer $n$.


The second line contains $n-1$ numbers. Each number is distinct and between $1$ and $n$ (inclusive).


## Output


Print the missing number.


## Constraints


- $2 \le n \le 2 \cdot 10^5$


## Example


Input:


```
5
2 3 1 5
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

void solve(){
  ll n, sum=0; cin>>n;
  fir(n-1){
    ll t; cin>>t;
    sum+=t;
  } 
  cout<<n*(n+1)/2 -sum<<endl;
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
