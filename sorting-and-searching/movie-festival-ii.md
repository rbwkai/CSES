# Movie Festival II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

In a movie festival, $n$ movies will be shown. Syrjälä's movie club consists of $k$ members, who will be all attending the festival.


You know the starting and ending time of each movie. What is the maximum total number of movies the club members can watch entirely if they act optimally?


## Input


The first input line has two integers $n$ and $k$: the number of movies and club members.


After this, there are $n$ lines that describe the movies. Each line has two integers $a$ and $b$: the starting and ending time of a movie.


## Output


Print one integer: the maximum total number of movies.


## Constraints


- $1 \le k \le n \le 2 \cdot 10^5$
- $1 \le a < b \le 10^9$


## Example


Input:


```
5 2
1 5
8 10
3 6
2 5
6 9
```


Output:


```
4
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
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, k; cin>>n>>k;
  vector<pi> v(n); fir(n) cin>>v[i].second, cin>>v[i].first;
  sort(v.begin(), v.end());

  ll res=0;
  multiset<ll> ms; fir(k) ms.insert(0);
  fir(n) if(ms.lower_bound(-v[i].second)!=ms.end()){
    ll et=*ms.lower_bound(-v[i].second);
    ms.erase(ms.find(et));
    ms.insert(-v[i].first);
    res++;
  }
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
