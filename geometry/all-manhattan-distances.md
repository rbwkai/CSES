# All Manhattan Distances

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a set of points, calculate the sum of all Manhattan distances between two point pairs.


## Input


The first line has an integer $n$: the number of points.


The following $n$ lines describe the points. Each line has two integers $x$ and $y$. You can assume that each point is distinct.


## Output


Print the sum of all Manhattan distances.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $-10^9 \le x, y \le 10^9$


## Example


Input:


```
5
1 1
3 2
2 4
2 1
4 5
```


Output:


```
36
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
using ll = __int128; //long long;
using vi = vector<ll>;
using pi = pair<ll, ll>;
using grid = vector<vi>;
 
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;

ll const mod = 1e9+7; //998244353;

ostream& operator<<(ostream& o, const __int128& x){ //+ve only
  if(x<10) return o << char('0' + x);
  return o<<x/10 << char('0' + x % 10);
}
void solve(){
  int n; cin>>n;
  vector<int> x(n), y(n); fir(n) cin>>x[i]>>y[i];
  sort(all(x)); sort(all(y));

  ll res=0;
  ll xm = 0, ym = 0;
  fir(n) res += (ll)i*x[i]-xm, xm+=x[i];
  fir(n) res += (ll)i*y[i]-ym, ym+=y[i];
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
