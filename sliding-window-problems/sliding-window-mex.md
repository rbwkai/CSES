# Sliding Window Mex

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers. Your task is to calculate the mex of each window of $k$ elements, from left to right.


The mex is the smallest nonnegative integer that does not appear in the array. For example, the mex for $[3,1,4,3,0,5]$ is $2$.


## Input


The first line contains two integers $n$ and $k$: the number of elements and the size of the window.


Then there are $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


## Output


Print $n-k+1$ values: the mex values.


## Constraints


- $1 \le k \le n \le 2 \cdot 10^5$
- $0 \le x_i \le 10^9$


## Example


Input:


```
8 3
1 2 1 0 5 1 1 0
```


Output:


```
0 3 2 2 0 2
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

struct NDV {
  ll res, pi, pe, k, nx;
  vi v;
  map<ll, ll> fq;
  set<ll> ms;
  NDV(ll _k): res(0), pi(0), pe(0), k(_k), nx(0), v(_k){
    ms.insert(0);
  }
  
  void insert(ll x){
    ms.erase(x);
    fq[x]++; nx++;
    if(!fq[nx]) ms.insert(nx);

    res=*ms.begin();
    v[pi]=x; pi=(pi+1)%k;
  }
  void erase(){
    fq[v[pe]] = max(fq[v[pe]]-1, 0LL);
    if(!fq[v[pe]]) ms.insert(v[pe]);

    res=*ms.begin();
    pe=(pe+1)%k;
  }
};

void solve(){
  ll n, k; cin>>n>>k;
  vi v(n); fir(n) cin>>v[i];

  NDV s(k);
  fir(k) s.insert(v[i]);
  cout<<s.res<<" ";
  
  fir(n-k){
    s.erase();
    s.insert(v[k+i]);
    cout<<s.res<<" ";
  } 
  cout<<en;
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
