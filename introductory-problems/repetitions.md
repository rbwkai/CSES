# Repetitions

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.


## Input


The only input line contains a string of $n$ characters.


## Output


Print one integer: the length of the longest repetition.


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
ATTCGGGA
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

void solve(){
  string s; cin>>s;
  ll n=s.size();
  ll l=0, r=0, mx=0;
  while(r<n){
    if(s[l]==s[r]) r++;
    else{
      mx=max(mx, r-l);
      l=r;
    }
  }
  mx=max(mx, r-l);
  cout<<mx<<endl;
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
