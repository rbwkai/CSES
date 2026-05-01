# Tower of Hanoi

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

The Tower of Hanoi game consists of three stacks (left, middle and right) and $n$ round disks of different sizes. Initially, the left stack has all the disks, in increasing order of size from top to bottom.


The goal is to move all the disks to the right stack using the middle stack. On each move you can move the uppermost disk from a stack to another stack. In addition, it is not allowed to place a larger disk on a smaller disk.


Your task is to find a solution that minimizes the number of moves.


## Input


The only input line has an integer $n$: the number of disks.


## Output


First print an integer $k$: the minimum number of moves.


After this, print $k$ lines that describe the moves. Each line has two integers $a$ and $b$: you move a disk from stack $a$ to stack $b$.


## Constraints


- $1 \le n \le 16$


## Example


Input:


```
2
```


Output:


```
3
1 2
1 3
2 3
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
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = LLONG_MAX-3e5; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  ll n; cin>>n;
  vi v(n);
  cout<<(1<<n)-1<<en;

  fir((1<<n)-1){
    ll ord=0;
    for(int t=i; t&1; t>>=1) ord++;

    ll at=v[ord];
    ll nx=(v[ord]+(1<<ord))%3;
    v[ord]=nx;

    vi s = {1, 2, 3};
    if((1<<(n-1))%3==1) s = {1, 3, 2};
    cout<<s[at]<<" "<<s[nx]<<en;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
