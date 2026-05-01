# Number Spiral

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:



Your task is to find out the number in row $y$ and column $x$.
## Input


The first input line contains an integer $t$: the number of tests.


After this, there are $t$ lines, each containing integers $y$ and $x$.


## Output


For each test, print the number in row $y$ and column $x$.


## Constraints


- $1 \le t \le 10^5$
- $1 \le y,x \le 10^9$


## Example


Input:


```
3
2 3
1 1
4 2
```


Output:


```
8
1
15
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
  ll y, x; cin>>y>>x;
  ll l=max(x, y), s=min(x, y), sq=(l-1)*(l-1), res;

  if((l%2)^(x>y)) res=sq+s;
  else res=l*l-s+1;
  cout<<res<<"\n";
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; cin>>tC;
  while(tC--){
    solve();
  }
}
```
