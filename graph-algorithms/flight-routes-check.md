# Flight Routes Check

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ cities and $m$ flight connections. Your task is to check if you can travel from any city to any other city using the available flights.


## Input


The first input line has two integers $n$ and $m$: the number of cities and flights. The cities are numbered $1,2,\dots,n$.


After this, there are $m$ lines describing the flights. Each line has two integers $a$ and $b$: there is a flight from city $a$ to city $b$. All flights are one-way flights.


## Output


Print "YES" if all routes are possible, and "NO" otherwise. In the latter case also print two cities $a$ and $b$ such that you cannot travel from city $a$ to city $b$. If there are several possible solutions, you can print any of them.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
4 5
1 2
2 3
3 1
1 4
3 4
```


Output:


```
NO
4 2
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

  ll tm=1;
  vi et(n+1, -1), mv(n+1, inf); 
  vi scc(n+1, -1); 
  stack<ll> sk;
  function<void(ll)> dfs=[&](ll at){
    et[at]=tm++; mv[at]=et[at];
    sk.push(at);

    for(ll to: edg[at]) if(et[to]){
      if(et[to]!=-1) mv[at]=min(mv[at], et[to]);
      else{
        dfs(to);
        mv[at]=min(mv[at], mv[to]);
      }
    }

    if(et[at]==mv[at]) while(1){
      ll cr=sk.top(); sk.pop();
      scc[cr]=at; et[cr]=0;
      if(cr==at) break;
    }
  }; dfs(1);

  fir(n) if(scc[i+1]!=scc[1]){
    ll s=1, f=i+1; if(scc[f]==-1) swap(s, f);
    cout<<"NO"<<en<<f<<" "<<s<<en;
    return;
  }
  cout<<"YES"<<en;
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
