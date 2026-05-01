# Subordinates

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given the structure of a company, your task is to calculate for each employee the number of their subordinates.


## Input


The first input line has an integer $n$: the number of employees. The employees are numbered $1,2,\dots,n$, and employee $1$ is the general director of the company.


After this, there are $n-1$ integers: for each employee $2,3,\dots,n$ their direct boss in the company.


## Output


Print $n$ integers: for each employee $1,2,\dots,n$ the number of their subordinates.


## Constraints


- $1 \le n \le 2 \cdot 10^5$


## Example


Input:


```
5
1 1 2 3
```


Output:


```
4 1 1 0 0
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

void solve(){
  ll n; cin>>n;
  grid edg(n+1); fir(n-1){
    ll t; cin>>t;
    edg[t].push_back(i+2);
  }
  
  vi ss(n+1);
  function<ll(ll)> rec=[&](ll cr){
    ll sz=1;
    for(ll to: edg[cr]) sz+=rec(to);
    return ss[cr]=sz;
  }; rec(1);

  fir(n) cout<<ss[i+1]-1<<ln;
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
