# Two Sets

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to divide the numbers $1,2,\ldots,n$ into two sets of equal sum.


## Input


The only input line contains an integer $n$.


## Output


Print "YES", if the division is possible, and "NO" otherwise.


After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.


## Constraints


- $1 \le n \le 10^6$


## Example 1


Input:


```
7
```


Output:


```
YES
4
1 2 4 7
3
3 5 6
```

## Example 2


Input:


```
6
```


Output:


```
NO
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

void solve(){
  ll n; cin>>n;
  ll rq = n*(n+1)/2;

  if(rq&1){
    cout<<"NO"<<en; return;
  }
  rq/=2;

  set<ll> x, y; ll a=n, b=n-1, c=n-2, d=n-3;
  while(d>0){
    x.insert(a); x.insert(d);
    y.insert(b); y.insert(c);
    a-=4, b-=4, c-=4, d-=4;
  }
  if(!d) x.insert(1), x.insert(2), y.insert(3);

  cout<<"YES"<<en;
  cout<<sz(x)<<en; for(ll p: x) cout<<p<<" "; cout<<en;
  cout<<sz(y)<<en; for(ll p: y) cout<<p<<" "; cout<<en;
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
