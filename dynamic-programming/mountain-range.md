# Mountain Range

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ mountains in a row, each with a specific height. You begin your hang gliding route from some mountain.


You can glide from mountain $a$ to mountain $b$ if mountain $a$ is taller than mountain $b$ and all mountains between $a$ and $b$.


What is the maximum number of mountains you can visit on your route?


## Input


The first line has an integer $n$: the number of mountains.


The next line has $n$ integers $h_1, h_2,\dots, h_n$: the heights of the mountains.


## Output:


Print one integer: the maximum number of mountains.


## Constraints


- $1\le n \le 2 \cdot 10^5$
- $1\le h_i \le 10^9$


## Example


Input:


```
10
20 15 17 35 25 40 12 19 13 12
```


Output:


```
5
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
  vi v(n); fir(n) cin>>v[i];

  vi cll(n), clr(n);
  stack<ll> ls, rs;
  fir(n){
    while(sz(ls) and v[ls.top()]<=v[i]) ls.pop();
    while(sz(rs) and v[rs.top()]<=v[ii]) rs.pop();

    cll[i]=(sz(ls)? ls.top(): -1);
    clr[ii]=(sz(rs)? rs.top(): n);

    ls.push(i); rs.push(ii);
  }

  grid edg(n); fir(n){
    if(cll[i]+1) edg[cll[i]].push_back(i);
    if(clr[i]-n) edg[clr[i]].push_back(i);
  }

  vi ord(n); fir(n) ord[i]=i;
  sort(ord.begin(), ord.end(), [&](ll i, ll j){return v[i]<v[j];});

  vi dp(n, 1); ll res=1;
  for(auto x: ord) for(ll t: edg[x]){
    dp[x]=max(dp[x], dp[t]+1);
    res=max(res, dp[x]);
  } 

  cout<<res<<en;
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
