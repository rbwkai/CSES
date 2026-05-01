# Counting Numbers

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to count the number of integers between $a$ and $b$ where no two adjacent digits are the same.


## Input


The only input line has two integers $a$ and $b$.


## Output


Print one integer: the answer to the problem.


## Constraints


- $0 \le a \le b \le 10^{18}$


## Example


Input:


```
123 321
```


Output:


```
171
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
 
#define fix(p) cout<<setprecision(p)<<fixed
#define mid(l, r) (l&r)+((l^r)>>1)
#define fir(a) for(int i=0; i<(a); ++i)
#define fjr(a) for(int j=0; j<a; ++j)
 
void solve(){
  ll a, b; cin>>a>>b;
  a--;
  vi va={}; while(a) {va.push_back(a%10); a/=10;} reverse(va.begin(), va.end());
  vi vb={}; while(b) {vb.push_back(b%10); b/=10;} reverse(vb.begin(), vb.end());

  ll dp[50][10][2];

  function<ll(vi, ll, ll, bool)> rec = [&](vi n, ll p, ll c, bool x){
    if(!p) memset(dp, -1, sizeof dp);
    if(p==n.size()) return 1LL;
    if(c+1 and dp[p][c][x]+1) return dp[p][c][x];

    ll res=0, ub=(x? n[p]: 9);
    fir(ub+1){
      if(i-c) res+=rec(n, p+1, (c==-1 and !i)? -1: i, x&&(i==ub)); 
    }
    if(c+1) dp[p][c][x] = res;
    return res;
  };
 
  ll resa=rec(va, 0, -1, 1);
  ll resb=rec(vb, 0, -1, 1);
  cout<<resb-resa<<endl;
}
 
int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
 
  int tt=1; //cin>>tt;
  while(tt--){
    solve();
  }
}
```
