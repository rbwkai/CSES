# Grundy's Game

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a heap of $n$ coins and two players who move alternately. On each move, a player chooses a heap and divides into two nonempty heaps that have a different number of coins. The player who makes the last move wins the game.


Your task is to find out who wins if both players play optimally.


## Input


The first input line contains an integer $t$: the number of tests.


After this, there are $t$ lines that describe the tests. Each line has an integer $n$: the number of coins in the initial heap.


## Output


For each test case, print "first" if the first player wins the game and "second" if the second player wins the game.


## Constraints


- $1 \le t \le 10^5$
- $1 \le n \le 10^6$


## Example


Input:


```
3
6
7
8
```


Output:


```
first
second
first
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


set<ll> lose = {0, 1, 2, 4, 7, 10, 20, 23, 26, 50, 53, 270,
                273, 276, 282, 285, 288, 316, 334, 337, 340,
                346, 359, 362, 365, 386, 389, 392, 566, 630,
                633, 636, 639, 673, 676, 682, 685, 923, 926,
                929, 932, 1222};
void solve(){
  ll n; cin>>n;
  cout<<(lose.find(n)==lose.end()? "first": "second")<<en;
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
