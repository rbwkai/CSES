# Path Queries II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a tree consisting of $n$ nodes. The nodes are numbered $1,2,\ldots,n$. Each node has a value.


Your task is to process following types of queries:



change the value of node $s$ to $x$
find the maximum value on the path between nodes $a$ and $b$.

## Input


The first input line contains two integers $n$ and $q$: the number of nodes and queries. The nodes are numbered $1,2,\ldots,n$.


The next line has $n$ integers $v_1,v_2,\ldots,v_n$: the value of each node.


Then there are $n-1$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


Finally, there are $q$ lines describing the queries. Each query is either of the form "1 $s$ $x$" or "2 $a$ $b$".


## Output


Print the answer to each query of type 2.


## Constraints


- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le a,b, s \le n$
- $1 \le v_i, x \le 10^9$


## Example


Input:


```
5 3
2 4 1 3 3
1 2
1 3
2 4
2 5
2 3 5
1 2 2
2 3 5
```


Output:


```
4 3
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
ll const mod = 998244353;
 

struct segtree{
  ll n;
  vi tree;
  segtree(int _n): n(_n), tree(2*_n, -1) {}

  void build(vi &v){
    fir(n) tree[n+i] = v[i];
    fir(n) if(ii) tree[ii] = max(tree[ii<<1], tree[ii<<1|1]);
  }
  ll query(int l, int r){
    ll res = -1;
    for(l+=n, r+=n; l<=r; l>>=1, r>>=1){
      if(l&1) res = max(res, tree[l++]);
      if(!(r&1)) res = max(res, tree[r--]);
    }
    return res;
  }
  void update(int p, ll val){
    p += n;
    tree[p] = val;
    for(p>>=1; p; p>>=1){
      tree[p] = max(tree[p<<1], tree[p<<1|1]);
    }
  }
};
 
void solve(){
  ll n, q; cin>>n>>q;
  vi v(n+1); fir(n) cin>>v[i+1];
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }

  ll root = 1;

  vi par(n+1), sze(n+1), dep(n+1),
     hvy(n+1), top(n+1), pos(n+1);
  function<void(ll, ll)> dfs=[&](ll at, ll pr){
    par[at]=pr; sze[at]=1;
    dep[at]=dep[pr]+1; hvy[at]=-1;

    for(ll to: edg[at]) if(to!=pr){
      dfs(to, at);
      sze[at] += sze[to];
      if(hvy[at]==-1 or sze[to]>sze[hvy[at]]) hvy[at]=to;
    }
  }; dfs(root, 0);

  vi hld;
  function<void(ll, ll)> dcm=[&](ll at, ll tp){
    top[at]=tp; pos[at]=sz(hld);
    hld.push_back(v[at]);

    if(hvy[at]!=-1) dcm(hvy[at], tp);
    for(ll to: edg[at]) if(to!=par[at] and to!=hvy[at]){
      dcm(to, to);
    }
  }; dcm(root, root);

  segtree stree(n);
  stree.build(hld);
  function<ll(ll, ll)> qry=[&](ll a, ll b){
    ll res = -1;
    while(top[a] != top[b]){
      if(dep[top[a]] < dep[top[b]]) swap(a, b);
      res = max(res, stree.query(pos[top[a]], pos[a]));
      a = par[top[a]];
    }

    if(dep[a] < dep[b]) swap(a, b);
    res = max(res, stree.query(pos[b], pos[a]));
    return res;
  };

  fir(q){
    ll t, a, b; cin>>t>>a>>b;
    if(t==1){
      stree.update(pos[a], b);
    }
    if(t==2){
      cout<<qry(a, b)<<" ";
    }
  }
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
