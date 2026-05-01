# Planets Queries I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are playing a game consisting of $n$ planets. Each planet has a teleporter to another planet (or the planet itself).


Your task is to process $q$ queries of the form: when you begin on planet $x$ and travel through $k$ teleporters, which planet will you reach?


## Input


The first input line has two integers $n$ and $q$: the number of planets and queries. The planets are numbered $1,2,\dots,n$.


The second line has $n$ integers $t_1,t_2,\dots,t_n$: for each planet, the destination of the teleporter. It is possible that $t_i=i$.


Finally, there are $q$ lines describing the queries. Each line has two integers $x$ and $k$: you start on planet $x$ and travel through $k$ teleporters.


## Output


Print the answer to each query.


## Constraints


- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le t_i \le n$
- $1 \le x \le n$
- $0 \le k \le 10^9$


## Example


Input:


```
4 3
2 1 1 4
1 2
3 4
4 1
```


Output:


```
1
2
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
//#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, q; cin>>n>>q;
  vi v(n); fir(n) cin>>v[i], v[i]--;

  grid bin(50, vi(n)); fir(n) bin[0][i]=v[i];
  fjr(49) fir(n) bin[j+1][i]=bin[j][ bin[j][i] ];

  while(q--){
    ll s, k; cin>>s>>k; s--;
    fir(50) if((k>>i)&1) s=bin[i][s];
    cout<<s+1<<en;
  }
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
