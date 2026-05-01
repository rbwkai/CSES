# Distinct Substrings

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Count the number of distinct substrings that appear in a string.


## Input


The only input line has a string of length $n$ that consists of characters a–z.


## Output


Print one integer: the number of substrings.


## Constraints


- $1 \le n \le 10^5$


## Example


Input:


```
abaa
```


Output:


```
8
```


Explanation: the substrings are a, b, aa, ab, ba, aba, baa and abaa.



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
#define sz(_O) (ll)_O.size()
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
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

struct SAM{
  struct S{
    ll len, link;
    vi next;
    S(ll l, ll k): len(l), link(k), next(26, -1) {}
  };

  vector<S> st;
  ll last;
  SAM(){
    st.push_back(S(0, -1));
    last = 0;
  }

  void extend(char c){
    ll cur = sz(st); c -= 'a';
    st.push_back(S(st[last].len+1, 0));

    ll p = last;
    while(p!=-1 and st[p].next[c]==-1){
      st[p].next[c] = cur;
      p = st[p].link;
    }

    if(p==-1) st[cur].link = 0;
    else{
      ll q = st[p].next[c];
      if(st[p].len+1 == st[q].len) st[cur].link = q;
      else{
        ll clone = sz(st);
        S cs = st[q]; cs.len = st[p].len+1;
        st.push_back(cs);

        while(p!=-1 and st[p].next[c]==q){
          st[p].next[c] = clone;
          p = st[p].link;
        }
        st[q].link = st[cur].link = clone;
      }
    }
    last = cur;
  }
};
void solve(){
  string s; cin>>s;
  SAM sam;
  for(ll c: s) sam.extend(c);
  
  ll r = 0;
  for(SAM::S x: sam.st) if(x.link!=-1) 
    r += x.len-sam.st[x.link].len;
  cout<< r <<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
