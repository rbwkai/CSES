# School Dance

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ boys and $m$ girls in a school. Next week a school dance will be organized. A dance pair consists of a boy and a girl, and there are $k$ potential pairs.


Your task is to find out the maximum number of dance pairs and show how this number can be achieved.


## Input


The first input line has three integers $n$, $m$ and $k$: the number of boys, girls, and potential pairs. The boys are numbered $1,2,\dots,n$, and the girls are numbered $1,2,\dots,m$.


After this, there are $k$ lines describing the potential pairs. Each line has two integers $a$ and $b$: boy $a$ and girl $b$ are willing to dance together.


## Output


First print one integer $r$: the maximum number of dance pairs. After this, print $r$ lines describing the pairs. You can print any valid solution.


## Constraints


- $1 \le n,m \le 500$
- $1 \le k \le 1000$
- $1 \le a \le n$
- $1 \le b \le m$


## Example


Input:


```
3 2 4
1 1
1 2
2 1
3 1
```


Output:


```
2
1 2
3 1
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
  ll n, m, k; cin>>n>>m>>k;
  grid edg(n+1); fir(k){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
  }

  vi pu(n+1), pv(m+1), dist(n+1);
  function<bool()> bft = [&](){
    queue<ll> qu; 
    fir(n){
      if(!pu[i+1]) dist[i+1]=0, qu.push(i+1);
      else dist[i+1]=inf;
    } 

    bool found = false;
    while(sz(qu)){
      ll u = qu.front(); qu.pop();
      for(ll v: edg[u]){
        ll u2 = pv[v];
        if(!u2) found = true;
        else if(dist[u2]==inf){
          dist[u2] = dist[u] + 1;
          qu.push(u2);
        }
      }
    }
    return found;
  };

  function<bool(ll)> dft = [&](ll u){
    for(ll v: edg[u]){
      ll u2 = pv[v];
      if(!u2 or (dist[u2]==dist[u]+1 and dft(u2))){
        pu[u] = v;
        pv[v] = u;
        return true;
      }
    }
    dist[u] = inf;
    return false;
  };

  ll mtch = 0;
  while(bft()){ //hopcroft karp
    fir(n) if(!pu[i+1] and dft(i+1)) mtch++;
  }
  cout<<mtch<<en;
  fir(n) if(pu[i+1]) cout<<i+1<<" "<<pu[i+1]<<en;
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
