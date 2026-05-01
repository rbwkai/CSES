# Movie Festival

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

In a movie festival $n$ movies will be shown. You know the starting and ending time of each movie. What is the maximum number of movies you can watch entirely?


## Input


The first input line has an integer $n$: the number of movies.


After this, there are $n$ lines that describe the movies. Each line has two integers $a$ and $b$: the starting and ending times of a movie.


## Output


Print one integer: the maximum number of movies.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a < b \le 10^9$


## Example


Input:


```
3
3 5
4 9
5 8
```


Output:


```
2
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
  ll n; cin>>n;
  vector<pi> v(n); fir(n){
    ll a, b; cin>>a>>b;
    v[i]={b, a};
  }
  sort(v.begin(), v.end());

  ll ce=0, res=0;
  fir(n){
    if(v[i].second>=ce) res++, ce=v[i].first;
  }
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
