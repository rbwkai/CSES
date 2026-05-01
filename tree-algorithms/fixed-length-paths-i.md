# Fixed-Length Paths I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a tree of $n$ nodes, your task is to count the number of distinct paths that consist of exactly $k$ edges.


## Input


The first input line contains two integers $n$ and $k$: the number of nodes and the path length. The nodes are numbered $1,2,\ldots,n$.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


## Output


Print one integer: the number of paths.


## Constraints


- $1 \le k \le n \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 2
1 2
2 3
3 4
3 5
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
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;
 
void solve(){
  ll n, k, ans=0; cin>>n>>k;
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }

  vi ss(n+1), vs(n+1);
  vi cnt(n+1, 0); ll mxd=0;
  function<void(ll, ll)> dfs=[&](ll c, ll p){
    ss[c]=1;
    for(ll t: edg[c]) if(t-p and !vs[t]){
      dfs(t, c);
      ss[c]+=ss[t];
    }
  };

  function<ll(ll, ll, ll)> ctr=[&](ll c, ll p, ll x){
    for(ll t: edg[c]) if(t-p and !vs[t] and ss[t]>x/2){
      return ctr(t, c, x);
    } 
    return c;
  };

  function<void(ll, ll, bool, ll)> rec=[&](ll cr, ll pr, bool md, ll dp){
    if(dp>k) return;
    mxd=max(mxd, dp);

    if(md) cnt[dp]++;
    else ans+=cnt[k-dp];

    for(ll to: edg[cr]) if(to-pr and !vs[to]){
      rec(to, cr, md, dp+1);
    }
  };

  function<void(ll)> slv=[&](ll nd){
    dfs(nd, 0);
    ll cnd=ctr(nd, 0, ss[nd]);
    vs[cnd]++;

    mxd=0; cnt[0]=1;
    for(ll ng: edg[cnd]) if(!vs[ng]){
      rec(ng, cnd, 0, 1);
      rec(ng, cnd, 1, 1);
    }
    fill(cnt.begin(), cnt.begin()+mxd+4, 0); cnt[0]=1;

    if(mxd*2<k) return;
    for(ll ng: edg[cnd]) if(!vs[ng]) slv(ng);
  }; slv(1);

  //for(auto [a, b]: cnt) cout<<a<<" "<<b<<en;
  cout<<ans<<en;
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
