# String Functions

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

We consider a string of $n$ characters, indexed $1,2,\dots,n$. Your task is to calculate all values of the following functions:


- $z(i)$ denotes the maximum length of a substring that begins at position $i$ and is a prefix of the string. In addition, $z(1)=0$.
- $\pi(i)$ denotes the maximum length of a substring that ends at position $i$, is a prefix of the string, and whose length is at most $i-1$.


Note that the function $z$ is used in the Z-algorithm, and the function $\pi$ is used in the KMP algorithm.


## Input


The only input line has a string of length $n$. Each character is between a–z.


## Output


Print two lines: first the values of the $z$ function, and then the values of the $\pi$ function.


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
abaabca
```


Output:


```
0 0 1 2 0 0 1
0 0 1 1 2 0 1
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

vi Z(string s){
  ll n = sz(s);

  vi z(n);
  ll l=0, r=0;
  fir(n) if(i){
    if(i>r){
      l = r = i;
      while(r<n and s[r-l]==s[r]) r++;
      z[i] = r-l; r--;
    }
    else{
      ll k = i-l;
      ll rem = r-i+1;
      if(z[k]<rem) z[i] = z[k];
      else{
        l = i;
        while(r+1<n and s[r+1-l]==s[r+1])
          r++;
        z[i] = r-l+1;
      }
    }
  }
  return z;
}
vi PI(string p){
  ll m = sz(p);

  vi dp(m);
  ll len = 0;
  fir(m) if(i){
    while(len>0 and p[len]!=p[i])
      len = dp[len-1];
    len += (p[len]==p[i]);
    dp[i] = len;
  }
  return dp;
}

void solve(){
  string s; cin>>s;
  ll n = sz(s);

  vi z = Z(s); fir(n) cout<<z[i]<<ln;
  vi p = PI(s); fir(n) cout<<p[i]<<ln;
  cout<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
