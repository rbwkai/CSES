# Message Route

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Syrjälä's network has $n$ computers and $m$ connections. Your task is to find out if Uolevi can send a message to Maija, and if it is possible, what is the minimum number of computers on such a route.


## Input


The first input line has two integers $n$ and $m$: the number of computers and connections. The computers are numbered $1,2,\dots,n$. Uolevi's computer is $1$ and Maija's computer is $n$.


Then, there are $m$ lines describing the connections. Each line has two integers $a$ and $b$: there is a connection between those computers.


Every connection is between two different computers, and there is at most one connection between any two computers.


## Output


If it is possible to send a message, first print $k$: the minimum number of computers on a valid route. After this, print an example of such a route. You can print any valid solution.


If there are no routes, print "IMPOSSIBLE".


## Constraints


- $2 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 5
1 2
1 3
1 4
2 3
5 4
```


Output:


```
3
1 4 5
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
    edg[v].push_back(u);
  }

  ll sr=n, ds=1;
  vi par(n+1), vis(n+1), depth(n+1); vis[sr]++;
  queue<ll> qu; qu.push(sr);
  ll d=0, cl=1, nl=0;
  while(sz(qu)){
    ll at=qu.front(); qu.pop(); cl--;
    depth[at]=d;

    if(at==ds) break;
    for(ll to: edg[at]) if(!vis[to]){
      qu.push(to);
      vis[to]++; par[to]=at; nl++;
    }
    if(!cl) d++, cl=nl, nl=0;
  }

  if(!par[ds]) cout<<"IMPOSSIBLE"<<en;
  else{
    cout<<depth[ds]+1<<en;
    while(ds!=sr) cout<<ds<<" ", ds=par[ds];
    cout<<sr<<en;
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
