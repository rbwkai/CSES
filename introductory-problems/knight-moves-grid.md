# Knight Moves Grid

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a knight on an $n \times n$ chessboard. For each square, print the minimum number of moves the knight needs to do to reach the top-left corner.


## Input


The only line has an integer $n$.


## Output


Print the number of moves for each square.


## Constraints


- $4 \le n \le 1000$


## Example


Input:


```
8
```


Output:


```
0 3 2 3 2 3 4 5 
3 4 1 2 3 4 3 4 
2 1 4 3 2 3 4 5 
3 2 3 2 3 4 3 4 
2 3 2 3 4 3 4 5 
3 4 3 4 3 4 5 4 
4 3 4 3 4 5 4 5 
5 4 5 4 5 4 5 6
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
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
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
    mint a=b, r=1;
    for( ; p; p>>=1, a=a*a) if(p&1) r=r*a;
    return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
}; 

void solve(){
  ll n; cin>>n;
  
  vi dx = {-1, 1, -2, 2, -2, 2, -1, 1};
  vi dy = {-2, -2, -1, -1, 1, 1, 2, 2};
  grid bd(n, vi(n, -1)); bd[0][0]=0;
  queue<pi> q; q.push({0, 0});

  while(sz(q)){
    auto [y, x] = q.front(); q.pop();
    fir(8){
      ll ny = y+dy[i], nx = x+dx[i];
      if(ny<0 or ny>=n 
      or nx<0 or nx>=n
      or bd[ny][nx]+1) continue;

      bd[ny][nx]=bd[y][x]+1;
      q.push({ny, nx});
    }
  }
  fjr(n) fir(n) cout<<bd[j][i]<<ln;
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
