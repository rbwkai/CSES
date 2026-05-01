# Company Queries II

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A company has $n$ employees, who form a tree hierarchy where each employee has a boss, except for the general director.


Your task is to process $q$ queries of the form: who is the lowest common boss of employees $a$ and $b$ in the hierarchy?


## Input


The first input line has two integers $n$ and $q$: the number of employees and queries. The employees are numbered $1,2,\dots,n$, and employee $1$ is the general director.


The next line has $n-1$ integers $e_2,e_3,\dots,e_n$: for each employee $2,3,\dots,n$ their boss.


Finally, there are $q$ lines describing the queries. Each line has two integers $a$ and $b$: who is the lowest common boss of employees $a$ and $b$?


## Output


Print the answer for each query.


## Constraints


- $1 \le n,q \le 2 \cdot 10^5$
- $1 \le e_i \le i-1$
- $1 \le a,b \le n$


## Example


Input:


```
5 3
1 1 3 3
4 5
2 5
1 4
```


Output:


```
3
1
1
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
  ll n, q; cin>>n>>q;
  grid edg(n+1); fir(n-1){
    ll t; cin>>t;
    edg[t].push_back(i+2);
  }

  grid bin(n+1, vi(20));
  vi dp(n+1);
  function<void(ll, ll)> rec=[&](ll c, ll p){
    for(auto t: edg[c]) if(t-p){
      dp[t]=dp[c]+1;
      bin[t][0]=c;
      rec(t, c);
    }
  }; rec(1, 0);

  fjr(20) fir(n) if(j) bin[i+1][j]=bin[ bin[i+1][j-1] ][j-1];
  
  while(q--){
    ll a, b; cin>>a>>b;
    if(dp[a]>dp[b]) swap(a, b);

    ll jr=dp[b]-dp[a];
    fir(20) if((jr>>i)&1) b=bin[b][i];

    if(a==b){
      cout<<a<<en; continue;
    }
    fir(20){
      ll ch=19-i;
      if(bin[a][ch]!=bin[b][ch]) a=bin[a][ch], b=bin[b][ch];
    }
    cout<<bin[a][0]<<en;
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
