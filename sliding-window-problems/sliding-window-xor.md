# Sliding Window Xor

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers. Your task is to calculate the bitwise xor of each window of $k$ elements, from left to right.


In this problem the input data is large and it is created using a generator.


## Input


The first line contains two integers $n$ and $k$: the number of elements and the size of the window.


The next line contains four integers $x$, $a$, $b$ and $c$: the input generator parameters. The input is generated as follows:


- $x_1=x$
- $x_i=(ax_{i-1}+b) \bmod c$ for $i=2,3,\dots,n$


## Output


Print the xor of all window xors.


## Constraints


- $1 \le k \le n \le 10^7$
- $0 \le x, a, b \le 10^9$
- $1 \le c \le 10^9$


## Example


Input:


```
8 5
3 7 1 11
```


Output:


```
0
```


Explanation: The input array is $[3,0,1,8,2,4,7,6]$. The windows are $[3,0,1,8,2]$, $[0,1,8,2,4]$, $[1,8,2,4,7]$ and $[8,2,4,7,6]$, and their xors are $8$, $15$, $8$ and $15$. Thus, the answer is $8 \oplus 15 \oplus 8 \oplus 15 = 0$.



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

struct XOR {
  ll res, pi, pe, k;
  vi v;
  XOR(ll _k): res(0), pi(0), pe(0), k(_k), v(_k) {}
  
  void insert(ll x){
    res^=x; v[pi]=x;
    pi=(pi+1)%k;
  }
  void erase(){
    res^=v[pe];
    pe=(pe+1)%k;
  }
};

void solve(){
  ll n, k; cin>>n>>k;
  ll x, a, b, c; cin>>x>>a>>b>>c;

  ll ans=0;
  XOR s(k);
  fir(k) s.insert(x), x=(x*a + b)%c;
  ans^=s.res;
  
  fir(n-k){
    s.erase();
    s.insert(x); x= (x*a + b)%c;
    ans^=s.res;
  } 
  cout<<ans<<en;
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
