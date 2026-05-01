# Counting Towers

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to build a tower whose width is $2$ and height is $n$. You have an unlimited supply of blocks whose width and height are integers.


For example, here are some possible solutions for $n=6$:



Given $n$, how many different towers can you build? Mirrored and rotated towers are counted separately if they look different.
## Input


The first input line contains an integer $t$: the number of tests.


After this, there are $t$ lines, and each line contains an integer $n$: the height of the tower.


## Output


For each test, print the number of towers modulo $10^9+7$.


## Constraints


- $1 \le t \le 100$
- $1 \le n \le 10^6$


## Example


Input:


```
3
2
6
1337
```


Output:


```
8
2864
640403945
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
  ll s=1, c=1;
  while(--n){
    tie(s, c)=make_tuple(4*s+c, s+2*c);
  }
  cout<<(s+c)%mod<<endl;
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
