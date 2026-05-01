# Distinct Values Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers and $q$ queries of the form: how many distinct values are there in a range $[a,b]$?


## Input


The first input line has two integers $n$ and $q$: the array size and number of queries.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the array values.


Finally, there are $q$ lines describing the queries. Each line has two integers $a$ and $b$.


## Output


For each query, print the number of distinct values in the range.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$
- $1 \le a \le b \le n$


## Example


Input:


```
5 3
3 2 3 1 2
1 3
2 4
1 5
```


Output:


```
2
3
3
```


---

## Solution

```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
using ll = long long;
using vi = vector<ll>;
using pii = pair<ll, ll>;
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
ll const mod = 998244353; //1e9+7

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
  vi v(n); fir(n) cin>>v[i];
  map<ll, ll> li;
  indexed_tree<ll> bt(n);

  grid qr(q); fir(q){
    ll a, b; cin>>a>>b; a--; b--;
    qr[i]={a, b, i};
  } sort(qr.begin(), qr.end());

  ll cq=q-1;
  vi res(q);
  for(int i=n-1; i>=0; i--){
    if(li.find(v[i])!=li.end()) bt.update(li[v[i]], -1);
    bt.update(i, 1); li[v[i]]=i;
    
    while(cq>=0 and qr[cq][0]==i) res[qr[cq][2]]=bt.query(qr[cq][1]), cq--;
  }
  fir(q) cout<<res[i]<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
