# Counting Divisors

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given $n$ integers, your task is to report for each integer the number of its divisors.


For example, if $x=18$, the correct answer is $6$ because its divisors are $1,2,3,6,9,18$.


## Input


The first input line has an integer $n$: the number of integers.


After this, there are $n$ lines, each containing an integer $x$.


## Output


For each integer, print the number of its divisors.


## Constraints


- $1 \le n \le 10^5$
- $1 \le x \le 10^6$


## Example


Input:


```
3
16
17
18
```


Output:


```
5
2
6
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
ll const mod = 1e9+7; //998244353;

vi dv(1e6+6, 0);
void pre(){
  ll N = 1e6+2;
  for(int i=1; i<=N; i++){
    for(int j=0; j<=N; j+=i) dv[j]++;
  }
}

void solve(){
  ll n; cin>>n;
  cout<<dv[n]<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  pre();

  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
