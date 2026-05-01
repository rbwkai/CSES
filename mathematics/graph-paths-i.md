# Graph Paths I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a directed graph that has $n$ nodes and $m$ edges. Your task is to count the number of paths from node $1$ to node $n$ with exactly $k$ edges.


## Input


The first input line contains three integers $n$, $m$ and $k$: the number of nodes and edges, and the length of the path. The nodes are numbered $1,2,\dots,n$.


Then, there are $m$ lines describing the edges. Each line contains two integers $a$ and $b$: there is an edge from node $a$ to node $b$.


## Output


Print the number of paths modulo $10^9+7$.


## Constraints


- $1 \le n \le 100$
- $1 \le m \le n(n-1)$
- $1 \le k \le 10^9$
- $1 \le a,b \le n$


## Example


Input:


```
3 4 8
1 2
2 3
3 1
3 2
```


Output:


```
2
```


Explanation: The paths are $1 \rightarrow 2 \rightarrow 3 \rightarrow 1 \rightarrow 2 \rightarrow 3 \rightarrow 1 \rightarrow 2 \rightarrow 3$ and $1 \rightarrow 2 \rightarrow 3 \rightarrow 2 \rightarrow 3 \rightarrow 2 \rightarrow 3 \rightarrow 2 \rightarrow 3$.



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

ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

grid mm(grid& a, grid& b){
  ll n=sz(a), c=sz(a[0]), m=sz(b[0]);
  grid res(n, vi(m, 0));

  fir(n) fjr(m) for(int k=0; k<c; ++k){
    res[i][j]+=a[i][k]*b[k][j];
    res[i][j]%=mod;
  }
  return res;
}

void solve(){
  ll n, m, x; cin>>n>>m>>x;
  grid mt(n, vi(n, 0)); fir(m){
    ll a, b; cin>>a>>b; 
    a--; b--; 
    mt[a][b]++;
  }

  grid res(n, vi(n, 0)); fir(n) res[i][i]=1;
  while(x){
    if(x&1) res=mm(res, mt);
    x>>=1;
    mt=mm(mt, mt);
  }
  cout<<res[0][n-1]<<en;
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
