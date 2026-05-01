# Rectangle Cutting

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an $a \times b$ rectangle, your task is to cut it into squares. On each move you can select a rectangle and cut it into two rectangles in such a way that all side lengths remain integers. What is the minimum possible number of moves?


## Input


The only input line has two integers $a$ and $b$.


## Output


Print one integer: the minimum number of moves.


## Constraints


- $1 \le a,b \le 500$


## Example


Input:


```
3 5
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
const ll mod = 1e9+7;

void solve(){
  ll a, b; cin>>a>>b;

  if(b>a) swap(a, b);
  grid dp(a+1, vi(b+1, -1));

  function<ll(ll, ll)> rec = [&](ll a, ll b){
    if(a<b) swap(a, b);
    if(a==b) return 0LL;
    if(dp[a][b]+1) return dp[a][b];

    ll mn=INT_MAX;
    for(int x=1; x<a; x++){
      mn=min(rec(x, b)+rec(a-x, b), mn);
    }
    for(int x=1; x<b; x++){
      mn=min(rec(x, a)+rec(b-x, a), mn);
    }
    return dp[a][b]=mn+1;
  };
  cout<<rec(a, b)<<endl;
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
