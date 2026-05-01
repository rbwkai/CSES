# Advertisement

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A fence consists of $n$ vertical boards. The width of each board is 1 and their heights may vary.


You want to attach a rectangular advertisement to the fence. What is the maximum area of such an advertisement?


## Input


The first input line contains an integer $n$: the width of the fence.


After this, there are $n$ integers $k_1,k_2,\ldots,k_n$: the height of each board.


## Output


Print one integer: the maximum area of an advertisement.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le k_i \le 10^9$


## Example


Input:


```
8
4 1 5 3 3 2 4 1
```


Output:


```
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
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n; cin>>n;
  vi v(n, 0); fir(n) cin>>v[i];

  ll res=0;
  stack<ll> st; st.push(-1);
  fir(n+1){
    while(sz(st)>1 and v[st.top()]>v[i]){
      ll h = v[st.top()]; st.pop();
      ll w = i-st.top() -1;
      res = max(res, h*w);
    }
    st.push(i);
  }
  cout<<res<<en;
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
