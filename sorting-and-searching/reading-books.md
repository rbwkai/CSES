# Reading Books

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ books, and Kotivalo and Justiina are going to read them all. For each book, you know the time it takes to read it.


They both read each book from beginning to end, and they cannot read a book at the same time. What is the minimum total time required?


## Input


The first input line has an integer $n$: the number of books.


The second line has $n$ integers $t_1,t_2,\dots,t_n$: the time required to read each book.


## Output


Print one integer: the minimum total time.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le t_i \le 10^9$


## Example


Input:


```
3
2 8 3
```


Output:


```
16
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

ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  ll n; cin>>n;
  ll mx=0, sm=0;
  fir(n){
    ll t; cin>>t;
    sm+=t; mx=max(mx, t);
  }
  cout<<max(2*mx, sm)<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
