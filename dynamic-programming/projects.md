# Projects

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ projects you can attend. For each project, you know its starting and ending days and the amount of money you would get as reward. You can only attend one project during a day.


What is the maximum amount of money you can earn?


## Input


The first input line contains an integer $n$: the number of projects.


After this, there are $n$ lines. Each such line has three integers $a_i$, $b_i$, and $p_i$: the starting day, the ending day, and the reward.


## Output


Print one integer: the maximum amount of money you can earn.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a_i \le b_i \le 10^9$
- $1 \le p_i \le 10^9$


## Example


Input:


```
4
2 4 4
3 6 6
6 8 2
5 7 3
```


Output:


```
7
```


---

## Solution

```cpp
//#pragma GCC optimize("Ofast,unroll-loops")
//#pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma,tune=native")

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
using ll = long long;
using vi = vector<ll>;
using pi = pair<ll, ll>;
using grid = vector<vi>;

template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = LLONG_MAX; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;

void solve(){
  ll n; cin>>n;
  grid v(n, vi(3)); fir(n) cin>>v[i][1]>>v[i][0]>>v[i][2];
  sort(v.begin(), v.end());

  vi dp(n+1, 0);
  fir(n){
    ll cs=v[i][1];
    ll l=-1, r=n-1;
    while(l<r){
      ll m=(l+r+1)/2;
      if(v[m][0]<cs) l=m;
      else r=m-1;
    }
    dp[i+1]=max(dp[i], dp[l+1]+v[i][2]);
  }
  cout<<dp[n]<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
