# Graph Paths II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a directed weighted graph having $n$ nodes and $m$ edges. Your task is to calculate the minimum path length from node $1$ to node $n$ with exactly $k$ edges.


## Input


The first input line contains three integers $n$, $m$ and $k$: the number of nodes and edges, and the length of the path. The nodes are numbered $1,2,\dots,n$.


Then, there are m lines describing the edges. Each line contains three integers $a$, $b$ and $c$: there is an edge from node $a$ to node $b$ with weight $c$.


## Output


Print the minimum path length. If there are no such paths, print $-1$.


## Constraints


- $1 \le n \le 100$
- $1 \le m \le n(n-1)$
- $1 \le k \le 10^9$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
3 4 8
1 2 5
2 3 4
3 1 1
3 2 2
```


Output:


```
27
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

ll const N = 2e6+6;
ll const inf = (1LL<<60); //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

grid mm(grid& a, grid& b){
  ll n=sz(a), c=sz(a[0]), m=sz(b[0]);
  grid res(n, vi(m, inf));

  fir(n) fjr(m) for(int k=0; k<c; ++k){
    res[i][j]=min(res[i][j], a[i][k]+b[k][j]);
  }
  return res;
}

void solve(){
  ll n, m, x; cin>>n>>m>>x;
  grid mt(n, vi(n, inf)); fir(m){
    ll a, b, c; cin>>a>>b>>c; 
    a--; b--; 
    mt[a][b]=min(mt[a][b], c);
  }

  grid res(n, vi(n, inf)); fir(n) res[i][i]=0;
  while(x){
    if(x&1) res=mm(mt, res);
    x>>=1;
    mt=mm(mt, mt);
  }
  cout<<(res[0][n-1]==inf? -1: res[0][n-1])<<en;
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
