# Finding a Centroid

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a tree of $n$ nodes, your task is to find a centroid, i.e., a node such that when it is appointed the root of the tree, each subtree has at most $\lfloor n/2 \rfloor$ nodes.


## Input


The first input line contains an integer $n$: the number of nodes. The nodes are numbered $1,2,…,n$.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


## Output


Print one integer: a centroid node. If there are several possibilities, you can choose any of them.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5
1 2
2 3
3 4
3 5
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
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;

void solve(){
  ll n; cin>>n;
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }
  
  vi ss(n+1, 1);
  function<void(ll, ll)> rec=[&](ll c, ll p){
    for(ll t: edg[c]) if(p-t){
      rec(t, c);
      ss[c]+=ss[t];
    }
  }; rec(1, 0);

  function<ll(ll, ll)> cnt=[&](ll c, ll p){
    ll mx=0, ms=0;
    for(ll t: edg[c]) if(p-t) if(ss[t]>mx) mx=ss[t], ms=t;

    if(mx<=n/2) return c;
    else return cnt(ms, c);
  };

  cout<<cnt(1, 0)<<en;
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
