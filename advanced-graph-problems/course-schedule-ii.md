# Course Schedule II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You want to complete $n$ courses that have requirements of the form "course $a$ has to be completed before course $b$".


You want to complete course $1$ as soon as possible. If there are several ways to do this, you want then to complete course $2$ as soon as possible, and so on.


Your task is to determine the order in which you complete the courses.


## Input


The first input line has two integers $n$ and $m$: the number of courses and requirements. The courses are numbered $1,2,\dots,n$.


Then, there are $m$ lines describing the requirements. Each line has two integers $a$ and $b$: course $a$ has to be completed before course $b$.


You can assume that there is at least one valid schedule.


## Output


Print one line having $n$ integers: the order in which you complete the courses.


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
4 2
2 1
2 3
```


Output:


```
2 1 3 4
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
#define F first
#define S second
#define pb push_back
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)



// 一心不乱
ll const N = 1e7;
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
  vi id(n+1);
  grid g(n+1); fir(m){
    ll a, b; cin>>a>>b;
    g[b].pb(a);
    id[a]++;
  }
  
  priority_queue<ll> pq;
  fir(n) if(!id[i+1]) pq.push(i+1);
  vi ans;
  while(sz(pq)){
    ll p = pq.top(); pq.pop();
    ans.pb(p);
    for(ll x: g[p]){
      id[x]--;
      if(!id[x]) pq.push(x);
    }
  }
  reverse(all(ans));
  fir(n) cout<<ans[i]<<ln;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
