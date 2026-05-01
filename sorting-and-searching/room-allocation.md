# Room Allocation

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a large hotel, and $n$ customers will arrive soon. Each customer wants to have a single room.


You know each customer's arrival and departure day. Two customers can stay in the same room if the departure day of the first customer is earlier than the arrival day of the second customer.


What is the minimum number of rooms that are needed to accommodate all customers? And how can the rooms be allocated?


## Input


The first input line contains an integer $n$: the number of customers.


Then there are $n$ lines, each of which describes one customer. Each line has two integers $a$ and $b$: the arrival and departure day.


## Output


Print first an integer $k$: the minimum number of rooms required.


After that, print a line that contains the room number of each customer in the same order as in the input. The rooms are numbered $1,2,\ldots,k$. You can print any valid solution.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a \le b \le 10^9$


## Example


Input:


```
3
1 2
2 4
4 4
```


Output:


```
2
1 2 1
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
  ll n; cin>>n;
  vector<tuple<ll, ll, ll>> v(2*n); fir(n){
    ll a, d; cin>>a>>d;
    v[2*i]={a, -1, i};
    v[2*i+1]={d, 1, i};
  } sort(v.begin(), v.end());
  
  set<ll> fs={}; ll mu=1;
  ll res=0; vi rs(n);

  ll cc=0; 
  fir(2*n){
    auto [w, x, y]=v[i];
    if(x==1){
      cc--; fs.insert(rs[y]);
    }else{
      cc++, res=max(res, cc);
      if(!fs.empty() and *fs.begin()<mu) rs[y]=*fs.begin(), fs.erase(rs[y]);
      else rs[y]=mu++;
    }
  }
  cout<<res<<en;
  fir(n) cout<<rs[i]<<ln;
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
