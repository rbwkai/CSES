# Coin Piles

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You have two coin piles containing $a$ and $b$ coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.


Your task is to efficiently find out if you can empty both the piles.


## Input


The first input line has an integer $t$: the number of tests.


After this, there are $t$ lines, each of which has two integers $a$ and $b$: the numbers of coins in the piles.


## Output


For each test, print "YES" if you can empty the piles and "NO" otherwise.


## Constraints


- $1 \le t \le 10^5$
- $0 \le a, b \le 10^9$


## Example


Input:


```
3
2 1
2 2
3 3
```


Output:


```
YES
NO
YES
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
  ll a, b; cin>>a>>b;
  if(a>b) swap(a, b);

  ll d=b-a;
  a-=d;
  if(a%3==0 and a>=0) cout<<"YES\n";
  else cout<<"NO\n";
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
