# Traffic Lights

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a street of length $x$ whose positions are numbered $0,1,\ldots,x$. Initially there are no traffic lights, but $n$ sets of traffic lights are added to the street one after another.


Your task is to calculate the length of the longest passage without traffic lights after each addition.


## Input


The first input line contains two integers $x$ and $n$: the length of the street and the number of sets of traffic lights.


Then, the next line contains $n$ integers $p_1,p_2,\ldots,p_n$: the position of each set of traffic lights. Each position is distinct.


## Output


Print the length of the longest passage without traffic lights after each addition.


## Constraints


- $1 \le x \le 10^9$
- $1 \le n \le 2 \cdot 10^5$
- $0 < p_i < x$


## Example


Input:


```
8 3
3 6 2
```


Output:


```
5 3 3
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
  vi v(k); fir(k) cin>>v[i];
  multiset<ll> lg={0, n}, iv={n};

  fir(k){
    auto ni=lg.upper_bound(v[i]);
    auto pi=prev(ni);
    ll ds=*ni-*pi;
    ll dp=v[i]-*pi, dn=*ni-v[i];
    lg.insert(v[i]); iv.erase(iv.find(ds));
    iv.insert(dp); iv.insert(dn);
    cout<<*iv.rbegin()<<" ";
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
