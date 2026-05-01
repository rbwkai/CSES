# Throwing Dice

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to calculate the number of ways to get a sum $n$ by throwing dice. Each throw yields an integer between $1 \ldots 6$.


For example, if $n=10$, some possible ways are $3+3+4$, $1+4+1+4$ and $1+1+6+1+1$.


## Input


The only input line contains an integer $n$.


## Output


Print the number of ways modulo $10^9+7$.


## Constraints


- $1 \le n \le 10^{18}$


## Example


Input:


```
8
```


Output:


```
125
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
    mt[a][b]=1;
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
