# Police Chase

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Kaaleppi has just robbed a bank and is now heading to the harbor. However, the police wants to stop him by closing some streets of the city.


What is the minimum number of streets that should be closed so that there is no route between the bank and the harbor?


## Input


The first input line has two integers $n$ and $m$: the number of crossings and streets. The crossings are numbered $1,2,\dots,n$. The bank is located at crossing $1$, and the harbor is located at crossing $n$.


After this, there are $m$ lines that describing the streets. Each line has two integers $a$ and $b$: there is a street between crossings $a$ and $b$. All streets are two-way streets, and there is at most one street between two crossings.


## Output


First print an integer $k$: the minimum number of streets that should be closed. After this, print $k$ lines describing the streets. You can print any valid solution.


## Constraints


- $2 \le n \le 500$
- $1 \le m \le 1000$
- $1 \le a,b \le n$


## Example


Input:


```
4 5
1 2
1 3
2 3
3 4
1 4
```


Output:


```
2
3 4
1 4
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
    ll u, v, w; cin>>u>>v;
    edg[u].push_back(v);
    edg[v].push_back(u);

    wts[{u, v}]+=1;
    wts[{v, u}]+=1;
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

  set<ll> ss;
  function<void(ll)> grw=[&](ll at){
    ss.insert(at);
    for(ll to: edg[at])
      if(!ss.count(to) and wts[{at, to}]>0){
        grw(to);
    }
  }; grw(1);

  fir(n){
    for(ll j: edg[i+1])
      if(ss.count(i+1) and !ss.count(j)){
      cout<<i+1<<" "<<j<<en;
    }
  }
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
