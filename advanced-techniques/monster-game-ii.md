# Monster Game II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are playing a game that consists of $n$ levels. Each level has a monster. On levels $1,2,\dots,n-1$, you can either kill or escape the monster. However, on level $n$ you must kill the final monster to win the game.


Killing a monster takes $sf$ time where $s$ is the monster's strength and $f$ is your skill factor. After killing a monster, you get a new skill factor  (lower skill factor is better). What is the minimum total time in which you can win the game?


## Input


The first input line has two integers $n$ and $x$: the number of levels and your initial skill factor.


The second line has $n$ integers $s_1,s_2,\dots,s_n$: each monster's strength.


The third line has $n$ integers $f_1,f_2,\dots,f_n$: your new skill factor after killing a monster.


## Output


Print one integer: the minimum total time to win the game.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x \le 10^6$
- $1 \le s_i, f_i \le 10^6$


## Example


Input:


```
5 100
50 20 30 90 30
60 20 20 10 90
```


Output:


```
2600
```


Explanation: The best way to play is to kill the second and fifth monster.



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
  ll n, x; cin>>n>>x;
  vi s(n); fir(n) cin>>s[i];
  vi f(n); fir(n) cin>>f[i];

  vi dp(n); 
  LCTree lct(0, 1e6+1);
  lct.insert(x, 0);
  fir(n){
    dp[i] = lct.query(s[i]);
    lct.insert(f[i], dp[i]);
  }
  cout<<dp[n-1]<<en;
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
