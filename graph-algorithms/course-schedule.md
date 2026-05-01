# Course Schedule

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You have to complete $n$ courses. There are $m$ requirements of the form "course $a$ has to be completed before course $b$". Your task is to find an order in which you can complete the courses.


## Input


The first input line has two integers $n$ and $m$: the number of courses and requirements. The courses are numbered $1,2,\dots,n$.


After this, there are $m$ lines describing the requirements. Each line has two integers $a$ and $b$: course $a$ has to be completed before course $b$.


## Output


Print an order in which you can complete the courses. You can print any valid order that includes all the courses.


If there are no solutions, print "IMPOSSIBLE".


## Constraints


- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a,b \le n$


## Example


Input:


```
5 3
1 2
3 1
4 5
```


Output:


```
3 4 1 5 2
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


void solve(){
  ll n, m; cin>>n>>m;
  vi in(n+1);
  grid edg(n+1); fir(m){
    ll u, v; cin>>u>>v;
    edg[u].push_back(v);
    in[v]++; 
  }

  queue<ll> qu; fir(n) if(!in[i+1]) qu.push(i+1);
  vi res(n); ll rp=0;
  while(sz(qu)){
    ll at=qu.front(); qu.pop();
    res[rp++]=at;
    for(auto nx: edg[at]){
      in[nx]--;
      if(!in[nx]) qu.push(nx);
    }
  }
  if(rp!=n) cout<<"IMPOSSIBLE"<<en;
  else fir(n) cout<<res[i]<<ln;
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
