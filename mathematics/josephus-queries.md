# Josephus Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider a game where there are $n$ children (numbered $1,2,\dots,n$) in a circle. During the game, every second child is removed from the circle, until there are no children left.


Your task is to process $q$ queries of the form: "when there are $n$ children, who is the $k$th child that will be removed?"


## Input


The first input line has an integer $q$: the number of queries.


After this, there are $q$ lines that describe the queries. Each line has two integers $n$ and $k$: the number of children and the position of the child.


## Output


Print $q$ integers: the answer for each query.


## Constraints


- $1 \le q \le 10^5$
- $1 \le k \le n \le 10^9$


## Example


Input:


```
4
7 1
7 3
2 2
1337 1313
```


Output:


```
2
6
1
1107
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
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

ll jphs(ll n, ll k){
  if(n==1 and k==1) return 1;
  if(2*k<=n) return 2*k;
  if(2*k==n+1) return 1;

  ll co=(n+1)/2;
  return 2*jphs(n/2, k-co) +2*(n&1) -1;
}

void solve(){
  ll n, k; cin>>n>>k;
  cout<<jphs(n, k)<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
