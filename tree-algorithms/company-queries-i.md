# Company Queries I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A company has $n$ employees, who form a tree hierarchy where each employee has a boss, except for the general director.


Your task is to process $q$ queries of the form: who is employee $x$'s boss $k$ levels higher up in the hierarchy?


## Input


The first input line has two integers $n$ and $q$: the number of employees and queries. The employees are numbered $1,2,\dots,n$, and employee $1$ is the general director.


The next line has $n-1$ integers $e_2,e_3,\dots,e_n$: for each employee $2,3,\dots,n$ their boss.


Finally, there are $q$ lines describing the queries. Each line has two integers $x$ and $k$: who is employee $x$'s boss $k$ levels higher up?


## Output


Print the answer for each query. If such a boss does not exist, print $-1$.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le e_i \le i-1$
- $1 \le x \le n$
- $1 \le k \le n$


## Example


Input:


```
5 3
1 1 3 3
4 1
4 2
4 3
```


Output:


```
3
1
-1
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
 
ll const inf = 0x3f3f3f3f3f3f;
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
  ll n, q; cin>>n>>q;
  grid edg(n+1); fir(n+1) if(i>1){
    ll p; cin>>p;
    edg[p].push_back(i);
  }

  vi dep(n+1), jmp(n+1), par(n+1);
  function<void(ll, ll)> dfs=[&](ll at, ll pr){
    dep[at]=dep[pr]+1;
    par[at]=pr;

    if(dep[jmp[jmp[pr]]]-dep[jmp[pr]]
    == dep[jmp[pr]]-dep[pr]) jmp[at]=jmp[jmp[pr]];
    else jmp[at]=pr;

    for(ll to: edg[at]) dfs(to, at);
  }; dfs(1, 0);

  fir(q){
    ll x, k; cin>>x>>k;
    ll tl = dep[x]-k;

    if(tl<1) cout<<-1<<en;
    else{
      while(dep[x]!=tl) x = (dep[jmp[x]]>=tl? jmp[x]: par[x]);
      cout<<x<<en;
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
