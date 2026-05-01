# Forest Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an $n \times n$ grid representing the map of a forest. Each square is either empty or contains a tree. The upper-left square has coordinates $(1,1)$, and the lower-right square has coordinates $(n,n)$.


Your task is to process $q$ queries of the form: how many trees are inside a given rectangle in the forest?


## Input


The first input line has two integers $n$ and $q$: the size of the forest and the number of queries.


Then, there are $n$ lines describing the forest. Each line has $n$ characters: . is an empty square and * is a tree.


Finally, there are $q$ lines describing the queries. Each line has four integers $y_1$, $x_1$, $y_2$, $x_2$ corresponding to the corners of a rectangle.


## Output


Print the number of trees inside each rectangle.


## Constraints


- $1 \le n \le 1000$
- $1 \le q \le 2 \cdot 10^5$
- $1 \le y_1 \le y_2 \le n$
- $1 \le x_1 \le x_2 \le n$


## Example


Input:


```
4 3
.*..
*.**
**..
****
2 2 3 4
3 1 3 1
1 1 2 2
```


Output:


```
3
1
2
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
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


template <class T> struct indexed_tree{
  int sn, sm;
  vector<vector<T>> bit;

  indexed_tree(int n, int m): sn(n), sm(m), bit(n+1, vector<T>(m+1, 0)) {}

  void update(int i, int j, T delta){
    for(++i; i<=sn; i+=i&-i)
      for(int jp=j+1; jp<=sm; jp+=jp&-jp)
        bit[i][jp]+=delta;
  }
  T query(int i, int j){
    T res=0;
    for(++i; i>0; i-=i&-i)
      for(int jp=j+1; jp>0; jp-=jp&-jp)
        res+=bit[i][jp];
    return res;
  }
  long unsigned int size(){return sn;}
};


void solve(){
  ll n, m; cin>>n>>m;
  grid v(n, vi(n, 0));
  indexed_tree<ll> bit(n, n);

  fir(n) fjr(n){
    char t; cin>>t;
    v[i][j]=t=='*';
    bit.update(i, j, t=='*');
  }
  while(m--){
    ll a, b, x, y; cin>>a>>b>>x>>y;
    a--; b--; x--; y--;
    ll res=bit.query(x, y)-bit.query(a-1, y)-bit.query(x, b-1)+bit.query(a-1, b-1);
    cout<<res<<en;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
