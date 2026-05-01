# Playlist

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a playlist of a radio station since its establishment. The playlist has a total of $n$ songs.


What is the longest sequence of successive songs where each song is unique?


## Input


The first input line contains an integer $n$: the number of songs.


The next line has $n$ integers $k_1,k_2,\ldots,k_n$: the id number of each song.


## Output


Print the length of the longest sequence of unique songs.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le k_i \le 10^9$


## Example


Input:


```
8
1 2 1 3 2 7 4 2
```


Output:


```
5
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
  vi v(n); fir(n) cin>>v[i];
  map<ll, ll> mp; 

  ll l=0, r=-1, res=0;
  while(r<n-1){
    ll nx=v[++r];
    if(mp.find(nx)!=mp.end() and mp[nx]>=l) l=mp[nx]+1;
    mp[nx]=r;
    res=max(res, r-l+1);
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
