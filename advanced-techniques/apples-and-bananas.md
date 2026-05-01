# Apples and Bananas

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ apples and $m$ bananas, and each of them has an integer weight between $1 \ldots k$. Your task is to calculate, for each weight $w$ between $2 \dots 2k$, the number of ways we can choose an apple and a banana whose combined weight is $w$.


## Input


The first input line contains three integers $k$, $n$ and $m$: the number $k$, the number of apples and the number of bananas.


The next line contains $n$ integers $a_1,a_2,\ldots,a_n$: weight of each apple.


The last line contains $m$ integers $b_1,b_2,\ldots,b_m$: weight of each banana.


## Output


For each integer $w$ between $2 \ldots 2k$ print the number of ways to choose an apple and a banana whose combined weight is $w$.


## Constraints


- $1 \le k,n,m \le 2 \cdot 10^5$
- $1 \le a_i \le k$
- $1 \le b_i \le k$


## Example


Input:


```
5 3 4
5 2 5
4 3 2 3
```


Output:


```
0 0 1 2 1 2 4 2 0
```


Explanation: For example for $w$ = $8$ there are $4$ different ways: we can pick an apple of weight $5$ in two different ways and a banana of weight $3$ in two different ways.



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
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353;

double const PI = acos(-1);
using cd = complex<double>;

vector<cd> fft(vector<cd>& a, bool invert){
  ll n=sz(a);
  vector<cd> f(a);

  vi rev(n);
  fir(n){
    rev[i] = (rev[i>>1]>>1) | ((i&1)*(n>>1));
    if(i<rev[i]) swap(f[i], f[rev[i]]); 
  }

  for(int len=2; len<=n; len<<=1){
    double ang = 2*PI/len * (invert? -1: 1);
    cd wlen(cos(ang), sin(ang));

    for(int i=0; i<n; i+=len){
      cd w(1);
      fjr(len/2){
        cd u = f[i+j], v=f[i+j+len/2]*w;
        f[i+j] = u+v;
        f[i+j+len/2] = u-v;
        w *= wlen;
      }
    }
  }

  if(invert) for(cd& x: f) x/=n;
  return f;
}

vi mul(vi& a, vi& b){
  ll n=1;
  while(n < sz(a)+sz(b)) n<<=1;
  vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
  fa.resize(n); fb.resize(n);

  vector<cd> fftA = fft(fa, false);
  vector<cd> fftB = fft(fb, false);

  vector<cd> fftC(n);
  fir(n) fftC[i] = fftA[i] * fftB[i];

  vector<cd> c = fft(fftC, true);
  vi res(n);
  fir(n) res[i] = round(c[i].real());
  return res;
}

void solve(){
  ll k, n, m, t; cin>>k>>n>>m;

  vi a(k+1), b(k+1);
  fir(n) cin>>t, a[t]++;
  fir(m) cin>>t, b[t]++;

  vi c = mul(a, b);
  fir(2*k +1) if(i>1) cout<<c[i]<<" ";
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
