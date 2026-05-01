# Polynomial Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to maintain an array of $n$ values and efficiently process the following types of queries:



Increase the first value in range $[a,b]$ by $1$, the second value by $2$, the third value by $3$, and so on.
Calculate the sum of values in range $[a,b]$.

## Input


The first input line has two integers $n$ and $q$: the size of the array and the number of queries.


The next line has $n$ values $t_1,t_2,\dots,t_n$: the initial contents of the array.


Finally, there are $q$ lines describing the queries. The format of each line is either "1 $a$ $b$" or "2 $a$ $b$".


## Output


Print the answer to each sum query.


## Constraints


- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le t_i \le 10^6$
- $1 \le a \le b \le n$


## Example


Input:


```
5 3
4 2 3 1 7
2 1 5
1 1 5
2 1 5
```


Output:


```
17
32
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
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)

ll const N = 2e6+6;
ll const inf = (1LL<<60); //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

struct segtree{
  ll n;
  vi tree;
  vector<pi> lazy;

  segtree(ll x): n(x), tree(4*x), lazy(4*x){}

  ll sigma(ll s, ll d, ll t){
    return t*(2*s + (t-1)*d)/2;
  }
  void build(vi &v, ll nd, ll lf, ll rt){
    if(lf==rt){
      tree[nd]=v[lf];
      lazy[nd]={0, 0};
      return;
    }
    ll md=lf+(rt-lf)/2;
    build(v, nd*2+1, lf, md);
    build(v, nd*2+2, md+1, rt);

    tree[nd]= tree[nd*2+1]+tree[nd*2+2];
    lazy[nd]={0, 0};
  }

  void push(ll nd, ll lf, ll rt){
    if(lf==rt) return;

    ll lc=nd*2+1, rc=nd*2+2, md=lf+(rt-lf)/2;
    ll st=lazy[nd].first, df=lazy[nd].second;

    lazy[lc].first+=st; lazy[lc].second+=df;
    tree[lc]+=sigma(st, df, md-lf+1);

    ll ss=st+df*(md-lf+1);
    lazy[rc].first+=ss; lazy[rc].second+=df;
    tree[rc]+=sigma(ss, df, rt-(md+1)+1);

    lazy[nd]={0, 0};
  }

  void update(ll nd, ll lf, ll rt, ll ul, ll ur, pi uv){
    push(nd, lf, rt);
    if(lf==ul and rt==ur){
      lazy[nd].first+=uv.first;
      lazy[nd].second+=uv.second;
      tree[nd]+=sigma(uv.first, uv.second, rt-lf+1);
      return;
    }
    if(ur<lf or ul>rt) return;

    ll md=lf+(rt-lf)/2; 
    ll st=uv.first, df=uv.second;
    update(nd*2+1, lf, md, ul, min(md, ur), uv);
    update(nd*2+2, md+1, rt, max(md+1, ul), ur, {st+(ul<md+1? (md+1-ul)*df: 0), df});
    tree[nd]=tree[nd*2+1]+tree[nd*2+2];
  }

  ll query(ll nd, ll lf, ll rt, ll ql, ll qr){
    push(nd, lf, rt);
    if(ql<=lf and rt<=qr) return tree[nd];
    if(ql>rt or qr<lf) return 0;

    int md=lf+(rt-lf)/2;
    ll tl = query(nd*2+1, lf, md, ql, qr);
    ll tr = query(nd*2+2, md+1, rt, ql, qr);
    return tl+tr;
  }
};

void solve(){
  ll n, q; cin>>n>>q;
  vi v(n); fir(n) cin>>v[i];

  segtree sg(n);
  sg.build(v, 0, 0, n-1);
  while(q--){
    ll t, a, b; cin>>t>>a>>b; t--, a--, b--;
    if(!t) sg.update(0, 0, n-1, a, b, {1, 1});
    else cout<<sg.query(0, 0, n-1, a, b)<<en;
  }
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
