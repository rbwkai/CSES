# Subtree Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a rooted tree consisting of $n$ nodes. The nodes are numbered $1,2,\ldots,n$, and node $1$ is the root. Each node has a value.


Your task is to process following types of queries:



change the value of node $s$ to $x$
calculate the sum of values in the subtree of node $s$

## Input


The first input line contains two integers $n$ and $q$: the number of nodes and queries. The nodes are numbered $1,2,\ldots,n$.


The next line has $n$ integers $v_1,v_2,\ldots,v_n$: the value of each node.


Then there are $n-1$ lines describing the edges. Each line contans two integers $a$ and $b$: there is an edge between nodes $a$ and $b$.


Finally, there are $q$ lines describing the queries. Each query is either of the form "1 $s$ $x$" or "2 $s$".


## Output


Print the answer to each query of type 2.


## Constraints


- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le a,b, s \le n$
- $1 \le v_i, x \le 10^9$


## Example


Input:


```
5 3
4 2 5 2 1
1 2
1 3
3 4
3 5
2 3
1 5 3
2 3
```


Output:


```
8
10
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
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


template <class T> struct indexed_tree{
  int ss;
  vector<T> bit;

  indexed_tree(int n): ss(n), bit(n+1, 0) {}

  void update(int i, T delta){
    for(++i; i<=ss; i+=i&-i) bit[i]+=delta;
  }
  T query(int i){
    T res=0;
    for(++i; i>0; i-=i&-i) res+=bit[i];
    return res;
  }
  long unsigned int size(){return ss;}
};

void solve(){
  ll n, q; cin>>n>>q;
  vi v(n+1); fir(n) cin>>v[i+1];
  grid edg(n+1); fir(n-1){
    ll a, b; cin>>a>>b;
    edg[a].push_back(b);
    edg[b].push_back(a);
  }
  
  vi ss(n+1, 1), sp(n+1);
  indexed_tree<ll> bit(n);
  ll in=0;
  function<void(ll, ll)> rec=[&](ll cr, ll pr){
    bit.update(in, v[cr]), sp[cr]=in;
    in++;
    
    for(ll to: edg[cr]) if(to-pr){
      rec(to, cr);
      ss[cr]+=ss[to];
    }
  }; rec(1, 0);

  while(q--){
    ll t; cin>>t;
    if(t==1){
      ll s, x; cin>>s>>x;
      ll cv=bit.query(sp[s])-bit.query(sp[s]-1);
      bit.update(sp[s], x-cv);
    }else{
      ll s; cin>>s;
      cout<<bit.query(sp[s]+ss[s]-1)-bit.query(sp[s]-1)<<en;
    }
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
