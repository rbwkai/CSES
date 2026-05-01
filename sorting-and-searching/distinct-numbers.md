# Distinct Numbers

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a list of $n$ integers, and your task is to calculate the number of distinct values in the list.


## Input


The first input line has an integer $n$: the number of values.


The second line has $n$ integers $x_1,x_2,\dots,x_n$.


## Output


Print one integers: the number of distinct values.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
5
2 3 2 2 3
```


Output:


```
2
```


---

## Solution

```cpp
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using vi = vector<ll>;
using pii = pair<ll, ll>;
using grid = vector<vi>;

#define fix(_oO) cout<<setprecision(_oO)<<fixed
#define fir(_oO) for(int i=0; i<_oO; ++i)
#define fjr(_oO) for(int j=0; j<_oO; ++j)

ll mod=1e9+7;

void solve(){
  set<ll> st; 
  ll n; cin>>n;
  while(n--){
    ll t; cin>>t;
    st.insert(t);
  }
  cout<<st.size()<<endl;
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; // cin>>tC;
  while(tC--){
    solve();
  }
}
```
