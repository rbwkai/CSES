# Lines and Queries I

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to efficiently process the following types of queries:



Add a line $ax+b$
Find the maximum point in any line at position $x$

## Input


The first line has an integer $n$: the number of queries.


The following $n$ lines describe the queries. The format of each line is either "1 $a$ $b$" or "2 $x$".


You may assume that the first query is of type 1.


## Output


Print the answer for each query of type 2.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $-10^9 \le a,b \le 10^9$
- $0 \le x \le 10^5$


## Example


Input:


```
6
1 1 2
2 1
2 3
1 0 4
2 1
2 3
```


Output:


```
3
5
4
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


// dp [j] = min{ f(i) + g(i)*h(j) : b + mx
// query h(j) : x
// insert g(i), f(i) : m, b
struct LCTree{
  struct Line{ll m, b;};
  struct Node{
    Line line;
    Node *l=nullptr, *r=nullptr;
    Node(Line _line): line(_line){}
  };
  
  ll L, R;
  Node *root = nullptr;
  LCTree(ll _L, ll _R): L(_L), R(_R) {}
  
  ll eval(Line& line, ll x) {return line.m*x + line.b;}
 
  void inBE(Line nwline, Node*& nd, ll lo, ll hi){
    if(!nd){
      nd = new Node(nwline);
      return;
    }
 
    ll md = lo + (hi-lo)/2;
    if(eval(nwline, md) <= eval(nd->line, md)) swap(nwline, nd->line);
    if(lo == hi) return;
 
    if (eval(nwline, lo) < eval(nd->line, lo))
      inBE(nwline, nd->l, lo, md);
    else if (eval(nwline, hi) < eval(nd->line, hi))
      inBE(nwline, nd->r, md+1, hi);
  }
  void insert(ll m, ll b){
    Line nline{m, b};
    inBE(nline, root, L, R);
  }
 
  ll query(ll x, Node* nd=nullptr, ll lo=inf, ll hi=inf) {
    if(lo==inf) nd=root, lo=L, hi=R;
    if(!nd) return inf;
 
    ll res = eval(nd->line, x);
    if (lo == hi) return res;
 
    ll md = lo + (hi-lo)/2;
    if (x<=md and nd->l)
      res = min(res, query(x, nd->l, lo, md));
    else if (x > md and nd->r)
      res = min(res, query(x, nd->r, md+1, hi));
    return res;
  }
 
  void clear(Node* nd) {
    if(!nd) return;
    clear(nd->l); clear(nd->r);
    delete nd;
  }
  ~LCTree() {clear(root);}
};
void solve(){
  ll q; cin>>q;
  LCTree LCT(-5, 1e5+5);
  fir(q){
    ll t; cin>>t;
    if(t==1){
      ll m, b; cin>>m>>b;
      LCT.insert(-m, -b);
    }
    if(t==2){
      ll x; cin>>x;
      cout<<-LCT.query(x)<<en;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt) solve();
}
```
