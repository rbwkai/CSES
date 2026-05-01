# Signal Processing

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given two integer sequences: a signal and a mask. Your task is to process the signal by moving the mask through the signal from left to right. At each mask position calculate the sum of products of aligned signal and mask values in the part where the signal and the mask overlap.


## Input


The first input line consists of two integers $n$ and $m$: the length of the signal and the length of the mask.


The next line consists of $n$ integers $a_1,a_2,\ldots,a_n$ defining the signal.


The last line consists of $m$ integers $b_1,b_2,\ldots,b_m$ defining the mask.


## Output


Print $n+m-1$ integers: the sum of products of aligned values at each mask position from left to right.


## Constraints


- $1 \le n,m \le 2 \cdot 10^5$
- $1 \le a_i,b_i \le 100$


## Example


Input:


```
5 3
1 3 2 1 4
1 2 3
```


Output:


```
3 11 13 10 16 9 4
```


Explanation: For example, at the second mask position the sum of aligned products is $2 \cdot 1 + 3 \cdot 3 = 11$.



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
  ll n, m; cin>>n>>m;
  vi a(n); fir(n) cin>>a[i];
  vi b(m); fir(m) cin>>b[i];
  reverse(b.begin(), b.end());

  vi c = mul(a, b);
  fir(n+m-1) cout<<c[i]<<" ";
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
