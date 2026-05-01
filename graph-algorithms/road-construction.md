# Road Construction

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ cities and initially no roads between them. However, every day a new road will be constructed, and there will be a total of $m$ roads.


A component is a group of cities where there is a route between any two cities using the roads. After each day, your task is to find the number of components and the size of the largest component.


## Input


The first input line has two integers $n$ and $m$: the number of cities and roads. The cities are numbered $1,2,\dots,n$.


Then, there are $m$ lines describing the new roads. Each line has two integers $a$ and $b$: a new road is constructed between cities $a$ and $b$.


You may assume that every road will be constructed between two different cities.


## Output


Print $m$ lines: the required information after each day.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 3
1 2
1 3
4 5
```


Output:


```
4 2
3 3
2 3
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

struct DSU{
  vi par, rnk;
  ll xr, cc;

  DSU(ll n): 
    par(n+1), rnk(n+1),
    xr(1), cc(n){
    fir(n+1) par[i]=i, rnk[i]=1;
  }

  ll root(ll x) {return (par[x]==x? x: par[x]=root(par[x]));}
  void link(ll x, ll y){
    x=root(x), y=root(y);
    if(x==y) return;

    if(rnk[x]<rnk[y]) swap(x, y);
    par[y]=x; rnk[x]+=rnk[y];
    xr=max(xr, rnk[x]); cc--;
  }
};

void solve(){
  ll n, m; cin>>n>>m;
  DSU dsu(n);

  while(m--){
    ll a, b; cin>>a>>b;
    dsu.link(a, b);
    cout<<dsu.cc<<" "<<dsu.xr<<en;
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
