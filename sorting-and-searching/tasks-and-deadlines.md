# Tasks and Deadlines

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You have to process $n$ tasks. Each task has a duration and a deadline, and you will process the tasks in some order one after another. Your reward for a task is $d-f$ where $d$ is its deadline and $f$ is your finishing time. (The starting time is $0$, and you have to process all tasks even if a task would yield negative reward.)


What is your maximum reward if you act optimally?


## Input


The first input line has an integer $n$: the number of tasks.


After this, there are $n$ lines that describe the tasks. Each line has two integers $a$ and $d$: the duration and deadline of the task.


## Output


Print one integer: the maximum reward.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le a,d \le 10^6$


## Example


Input:


```
3
6 10
8 15
5 12
```


Output:


```
2
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
  vector<pi> v(n); fir(n) cin>>v[i].first>>v[i].second;
  sort(v.begin(), v.end());

  ll tp=0, res=0;
  fir(n){
    res+=v[i].second-(tp+v[i].first);
    tp+=v[i].first;
  }
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
