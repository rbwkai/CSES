# Sliding Window Mode

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers. Your task is to calculate the mode each window of $k$ elements, from left to right.


The mode is the most frequent element in an array. If there are several possible modes, choose the smallest of them.


## Input


The first line contains two integers $n$ and $k$: the number of elements and the size of the window.


Then there are $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


## Output


Print $n-k+1$ values: the modes.


## Constraints


- $1 \le k \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
8 3
1 2 3 2 5 2 4 4
```


Output:


```
1 2 2 2 2 4
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
using pii = pair<ll, ll>;
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

struct MODE {
  ll res, pi, pe, k;
  vi v;
  map<ll, ll> fq;
  set<pii> fs;
  MODE(ll _k): res(0), pi(0), pe(0), k(_k), v(_k) {}
  
  void insert(ll x){
    fs.erase({-fq[x], x});
    fq[x]++;
    fs.insert({-fq[x], x});

    res=fs.begin()->second;
    v[pi]=x; pi=(pi+1)%k;
  }
  void erase(){
    fs.erase({-fq[v[pe]], v[pe]});
    fq[v[pe]]--;
    fs.insert({-fq[v[pe]], v[pe]});

    res=fs.begin()->second;
    pe=(pe+1)%k;
  }
};

void solve(){
  ll n, k; cin>>n>>k;
  vi v(n); fir(n) cin>>v[i];

  MODE s(k);
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
