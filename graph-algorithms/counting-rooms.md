# Counting Rooms

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a map of a building, and your task is to count the number of its rooms. The size of the map is $n \times m$ squares, and each square is either floor or wall. You can walk left, right, up, and down through the floor squares.


## Input


The first input line has two integers $n$ and $m$: the height and width of the map.


Then there are $n$ lines of $m$ characters describing the map. Each character is either . (floor) or # (wall).


## Output


Print one integer: the number of rooms.


## Constraints


- $1 \le n,m \le 1000$


## Example


Input:


```
5 8
########
#..#...#
####.#.#
#..#...#
########
```


Output:


```
3
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
  ll n, m; cin>>n>>m;
  string s, t; fir(n) cin>>t, s+=t;

  function<void(ll)> dfs=[&](ll id){
    if(s[id]=='#') return;
    s[id]='#';

    if(id%m != m-1) dfs(id+1);
    if(id%m != 0) dfs(id-1);

    if(id/m != n-1) dfs(id+m);
    if(id/m != 0) dfs(id-m);
  };
  
  ll r=0;
  fir(n*m) if(s[i]=='.') r++, dfs(i);
  cout<<r<<en;
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
