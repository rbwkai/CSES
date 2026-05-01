# Repeating Substring

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A repeating substring is a substring that occurs in two (or more) locations in the string. Your task is to find the longest repeating substring in a given string.


## Input


The only input line has a string of length $n$ that consists of characters a–z.


## Output


Print the longest repeating substring. If there are several possibilities, you can print any of them. If there is no repeating substring, print $-1$.


## Constraints


- $1 \le n \le 10^5$


## Example


Input:


```
cabababc
```


Output:


```
abab
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
#define all(_O) _O.begin(), _O.end()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)

ll const N = 1e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

vi SA(string& s){
  ll n = sz(s);
  vi sa(n), rank(n), tmp(n);

  fir(n) sa[i]=i, rank[i]=s[i];

  for(ll k=1; ; k<<=1){
    auto cmp=[&](ll i, ll j){
      if(rank[i]!=rank[j]) return rank[i]<rank[j];
      ll ri = (i+k<n)? rank[i+k]: -1;
      ll rj = (j+k<n)? rank[j+k]: -1;
      return ri<rj;
    }; sort(all(sa), cmp);

    tmp[sa[0]]=0;
    fir(n) if(i){
      tmp[sa[i]] = tmp[sa[i-1]]+(cmp(sa[i-1], sa[i])? 1: 0);
    }
    rank = tmp;
    if(rank[sa[n-1]]==n-1) break;
  }
  return sa;
}
vi LCP(string& s, vi& sa){
  ll n = sz(s);
  vi rank(n), lcp(n);

  fir(n) rank[sa[i]] = i;

  ll h=0;
  fir(n){
    if(rank[i]>0){
      ll j = sa[rank[i]-1];
      while(i+h<n and j+h<n and s[i+h]==s[j+h]) h++;
      lcp[rank[i]] = h;
      if(h>0) h--;
    }
  }
  return lcp;
}

void solve(){
  string s; cin>>s;
  ll n = sz(s);

  vi sa = SA(s);
  vi lcp = LCP(s, sa);
  ll len = *max_element(all(lcp));
  fir(n) if(len and lcp[i]==len){
    cout<<s.substr(sa[i], len)<<en;
    return;
  }
  cout<<-1<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
