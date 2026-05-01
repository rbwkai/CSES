# Tree Distances I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a tree consisting of $n$ nodes.


Your task is to determine for each node the maximum distance to another node.


## Input


The first input line contains an integer $n$: the number of nodes. The nodes are numbered $1,2,\ldots,n$.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


## Output


Print $n$ integers: for each node $1,2,\ldots,n$, the maximum distance to another node.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5
1 2
1 3
3 4
3 5
```


Output:


```
2 3 2 3 3
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
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

struct mint{
  ll v; 
  mint(ll _v=0) {v = (_v%mod +mod)%mod;}

  friend mint operator+(const mint& a, const mint& b){ return mint(a.v + b.v); }
  friend mint operator-(const mint& a, const mint& b){ return mint(a.v - b.v); }
  friend mint operator*(const mint& a, const mint& b){ return mint(a.v * b.v); }
  friend mint operator/(const mint& a, const mint& b){ return a*minv(b); }
  friend mint mpow(const mint& b, ll p){
    mint a=b, r=1; for( ; p; p>>=1, a=a*a) if(p&1) r=r*a; return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
}; 


void solve(){
  ll n; cin>>n;
  grid edg(n+1); fir(n-1){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
    edg[v].push_back(u);
  }

  function<void(ll, ll, vi&)> dfs=[&](ll at, ll pr, vi& dis){
    dis[at] = dis[pr]+1;
    for(ll to: edg[at]) if(to!=pr) dfs(to, at, dis);
  };

  vi rd(n+1); dfs(1, 0, rd);
  ll a = max_element(rd.begin(), rd.end()) - rd.begin();
  vi da(n+1); dfs(a, 0, da);
  ll b = max_element(da.begin(), da.end()) - da.begin();
  vi db(n+1); dfs(b, 0, db);

  fir(n) cout<<max(da[i+1], db[i+1])-1<<ln;
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
