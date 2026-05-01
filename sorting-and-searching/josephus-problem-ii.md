# Josephus Problem II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a game where there are $n$ children (numbered $1,2,\dots,n$) in a circle. During the game, repeatedly $k$ children are skipped and one child is removed from the circle. In which order will the children be removed?


## Input


The only input line has two integers $n$ and $k$.


## Output


Print $n$ integers: the removal order.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $0 \le k \le 10^9$


## Example


Input:


```
7 2
```


Output:


```
3 6 2 7 5 1 4
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

ll const inf = LLONG_MAX-3e5; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  ll n, k; cin>>n>>k;
  ordered_set<ll> os; fir(n) os.insert(i+1);

  ll id=0;
  while(os.size()){
    id=(id+k)%os.size();
    ll nx=*os.find_by_order(id);
    cout<<nx<<" ";
    os.erase(nx);
  }
  cout<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
