# Longest Flight Route

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Uolevi has won a contest, and the prize is a free flight trip that can consist of one or more flights through cities. Of course, Uolevi wants to choose a trip that has as many cities as possible.


Uolevi wants to fly from Syrjälä to Lehmälä so that he visits the maximum number of cities. You are given the list of possible flights, and you know that there are no directed cycles in the flight network.


## Input


The first input line has two integers $n$ and $m$: the number of cities and flights. The cities are numbered $1,2,\dots,n$. City $1$ is Syrjälä, and city $n$ is Lehmälä.


After this, there are $m$ lines describing the flights. Each line has two integers $a$ and $b$: there is a flight from city $a$ to city $b$. Each flight is a one-way flight.


## Output


First print the maximum number of cities on the route. After this, print the cities in the order they will be visited. You can print any valid solution.


If there are no solutions, print "IMPOSSIBLE".


## Constraints


- $2 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 5
1 2
2 5
1 3
3 4
4 5
```


Output:


```
4
1 3 4 5
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
  grid edg(n+1); fir(m){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
  }

  vi ddp(n+1, -inf), tdp(n+1, -1);
  function<void(ll)> rec=[&](ll at){
    if(ddp[at]+inf) return;
    if(at==n){ddp[n]=0; return;}

    for(ll to: edg[at]){
      rec(to);
      if(ddp[at]<ddp[to]+1) ddp[at]=ddp[to]+1, tdp[at]=to; 
    }
  }; rec(1);
  
  if(ddp[n]){cout<<"IMPOSSIBLE"<<en; return;}
  cout<<ddp[1]+1<<en<<1<<" ";
  ll at=1;
  while(at!=n) cout<<(at=tdp[at])<<" ";
  cout<<en;
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
