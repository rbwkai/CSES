# Edit Distance

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

The edit distance between two strings is the minimum number of operations required to transform one string into the other.


The allowed operations are:


- Add one character to the string.
- Remove one character from the string.
- Replace one character in the string.


For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.


Your task is to calculate the edit distance between two strings.


## Input


The first input line has a string that contains $n$ characters between A–Z.


The second input line has a string that contains $m$ characters between A–Z.


## Output


Print one integer: the edit distance between the strings.


## Constraints


- $1 \le n,m \le 5000$


## Example


Input:


```
LOVE
MOVIE
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
  string s; cin>>s; ll sl=s.size(); 
  string t; cin>>t; ll tl=t.size(); 
  
  grid dp(sl+1, vi(tl+1, INT_MAX));
  for(int r=sl; r>=0; r--){
    for(int c=tl; c>=0; c--){
      if(r==sl and c==tl) dp[r][c]=0;
      if(r!=sl) dp[r][c]=min(dp[r][c], dp[r+1][c]+1);
      if(c!=tl) dp[r][c]=min(dp[r][c], dp[r][c+1]+1);
      if(r!=sl and c!=tl) dp[r][c]=min(dp[r][c], dp[r+1][c+1]+(s[r]!=t[c]));
    }
  }
  cout<<dp[0][0]<<endl;
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
