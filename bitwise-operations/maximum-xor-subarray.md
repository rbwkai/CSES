# Maximum Xor Subarray

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, your task is to find the maximum xor sum of a subarray.


## Input


The first line has an integer $n$: the size of the array.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


## Output


Print one integer: the maximum xor sum in a subarray.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $0 \le x_i \le 10^9$


## Example


Input:


```
4
5 1 5 9
```


Output:


```
13
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
ll const mod = 998244353;

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

struct Trie{
  ll A, S;
  struct Node{
    vector<Node*> nxt;
    Node(): nxt(2, nullptr){}
  };
  Node* root;

  Trie(): A(2), S(64){
    root = new Node();
  }

  void insert(ll x){
    Node* cur = root;
    fir(S){
      bool bt = (x>>ii)&1;
      if(!cur->nxt[bt]) cur->nxt[bt] = new Node();
      cur = cur->nxt[bt];
    }
  }
  ll find(ll x){
    Node* cur = root;
    ll mtch = 0;
    fir(S){
      ll bt = (x>>ii)&1;
      if(cur->nxt[!bt]) mtch|=((!bt)<<ii), cur=cur->nxt[!bt];
      else mtch|=(bt<<ii), cur=cur->nxt[bt];
    }
    return mtch;
  }

  void clear(Node* node) {
    if (!node) return;
    for(Node* child: node->nxt)
      clear(child);
    delete node;
  }
  ~Trie() {
    clear(root);
  }
};

void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) cin>>v[i];

  vi px(n+1, 0); fir(n) px[i+1]=px[i]^v[i]; 
  Trie t; t.insert(px[0]);
  ll res=0;
  fir(n){
    res = max(res, px[i+1] ^ t.find(px[i+1]));
    t.insert(px[i+1]);
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
