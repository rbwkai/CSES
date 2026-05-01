# Distinct Subsequences

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a string. You can remove any number of characters from it, but you cannot change the order of the remaining characters.


How many different strings can you generate?


## Input


The first input line contains a string of size $n$. Each character is one of a–z.


## Output


Print one integer: the number of strings modulo $10^9+7$.


## Constraints


- $1 \le n \le 5 \cdot 10^5$


## Example


Input:


```
aybabtu
```


Output:


```
103
```


---

## Solution

```cpp
//#pragma GCC optimize("Ofast,unroll-loops")
//#pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma,tune=native")

#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using vi = vector<ll>;
using pi = pair<ll, ll>;
using grid = vector<vi>;

#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)

ll const N = 1e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  string s; cin>>s;
  ll n = sz(s);

  vi dp(n+1); dp[0]=1;
  vi last(26, -1);
  fir(n){
    ll c = s[i]-'a';
    if(last[c]!=-1){
      dp[i+1] = (dp[i+1]-dp[last[c]]+mod);
    }
    dp[i+1] += 2*dp[i];
    dp[i+1]%=mod; last[c]=i;
  }
  cout<<(dp[n]-1+mod)%mod<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
