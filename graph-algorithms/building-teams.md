# Building Teams

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ pupils in Uolevi's class, and $m$ friendships between them. Your task is to divide the pupils into two teams in such a way that no two pupils in a team are friends. You can freely choose the sizes of the teams.


## Input


The first input line has two integers $n$ and $m$: the number of pupils and friendships. The pupils are numbered $1,2,\dots,n$.


Then, there are $m$ lines describing the friendships. Each line has two integers $a$ and $b$: pupils $a$ and $b$ are friends.


Every friendship is between two different pupils. You can assume that there is at most one friendship between any two pupils.


## Output


Print an example of how to build the teams. For each pupil, print "1" or "2" depending on to which team the pupil will be assigned. You can print any valid team.


If there are no solutions, print "IMPOSSIBLE".


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
1 2 2 1 2
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

  vi vis(n+1);
  function<ll(ll)> dfs=[&](ll at){
    for(ll to: edg[at]){
      if(vis[to]==vis[at]) return -1LL;
      else if(!vis[to]){
        vis[to]=3-vis[at];
        if(dfs(to)==-1) return -1LL;
      }
    }
    return 0LL;
  };
  
  fir(n) if(!vis[i+1]){
    vis[i+1]=1;
    if(dfs(i+1)==-1){
      cout<<"IMPOSSIBLE"<<en;
      return;
    }
  }
  fir(n) cout<<vis[i+1]<<ln;
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
