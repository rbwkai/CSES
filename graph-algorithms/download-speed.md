# Download Speed

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a network consisting of $n$ computers and $m$ connections. Each connection specifies how fast a computer can send data to another computer.


Kotivalo wants to download some data from a server. What is the maximum speed he can do this, using the connections in the network?


## Input


The first input line has two integers $n$ and $m$: the number of computers and connections. The computers are numbered $1,2,\dots,n$. Computer $1$ is the server and computer $n$ is Kotivalo's computer.


After this, there are $m$ lines describing the connections. Each line has three integers $a$, $b$ and $c$: computer $a$ can send data to computer $b$ at speed $c$.


## Output


Print one integer: the maximum speed Kotivalo can download data.


## Constraints


- $1 \le n \le 500$
- $1 \le m \le 1000$
- $1 \le a,b \le n$
- $1 \le c \le 10^9$


## Example


Input:


```
4 5
1 2 3
2 4 2
1 3 4
3 4 5
4 1 3
```


Output:


```
6
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
  ll n, m; cin>>n>>m;
  map<pi, ll> wts;
  grid edg(n+1); fir(m){
    ll u, v, w; cin>>u>>v>>w;
    edg[u].push_back(v);
    edg[v].push_back(u);

    wts[{u, v}]+=w;
    wts[{v, u}]+=0;
  }

  ll flow = 0;
  vi vis(n+1); ll thrhd;
  function<ll(ll, ll)> dfs=[&](ll at, ll bn){
    vis[at]=1;
    if(at==n) return bn;
    for(ll to: edg[at]){
      ll ew = wts[{at, to}];
      if(!vis[to] and ew>=thrhd){
        ll r = dfs(to, min(bn, ew));
        if(r!=-1){
          wts[{at, to}] -= r;
          wts[{to, at}] += r;
          return r;
        }
      }
    } 
    return -1ll;
  };

  fir(32){
    thrhd = (1ll<<ii);
    while(true){
      fill(vis.begin(), vis.end(), 0ll);
      ll r = dfs(1, inf);
      if(r==-1) break;
      flow += r;
    }
  }
  cout<<flow<<en;
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
