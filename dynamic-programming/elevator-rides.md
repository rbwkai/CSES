# Elevator Rides

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ people who want to get to the top of a building which has only one elevator. You know the weight of each person and the maximum allowed weight in the elevator. What is the minimum number of elevator rides?


## Input


The first input line has two integers $n$ and $x$: the number of people and the maximum allowed weight in the elevator.


The second line has $n$ integers $w_1,w_2,\dots,w_n$: the weight of each person.


## Output


Print one integer: the minimum number of rides.


## Constraints


- $1 \le n \le 20$
- $1 \le x \le 10^9$
- $1 \le w_i \le x$


## Example


Input:


```
4 10
4 8 6 1
```


Output:


```
2
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
  ll n, w; cin>>n>>w;
  vi v(n); fir(n) cin>>v[i];

  vector<pii> dp((1<<n), {-1, -1}); dp[0]={0, w};
  function<pii(ll)> rec = [&](ll m){
    pii df={-1, -1};
    if(dp[m]!=df) return dp[m];
    pii mx={INT_MAX, INT_MAX};
    fir(31){
      if((m>>i) & 1){
        pii cr;
        auto [a, b]=rec(m^(1<<i));
        if(b+v[i]<=w) cr={a, b+v[i]};
        else cr={a+1, v[i]};
        mx=min(mx, cr);
      }
    }
    return dp[m]=mx;
  };
  cout<<(rec((1<<n)-1).first)<<endl;
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
