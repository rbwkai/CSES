# Increasing Subsequence

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array containing $n$ integers. Your task is to determine the longest increasing subsequence in the array, i.e., the longest subsequence where every element is larger than the previous one.


A subsequence is a sequence that can be derived from the array by deleting some elements without changing the order of the remaining elements.


## Input


The first line contains an integer $n$: the size of the array.


After this there are $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


## Output


Print the length of the longest increasing subsequence.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
8
7 3 5 3 6 2 9 8
```


Output:


```
4
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
const ll mod = 1e9+7;

void solve(){
  ll n; cin>>n;
  set<ll> st;
  fir(n){
    ll t; cin>>t;
    auto it=st.lower_bound(t);
    if(it==st.end()) st.insert(t);
    else{
      st.erase(it);
      st.insert(t);
    }
  }
  cout<<st.size()<<endl;
}


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; //cin>>tC;
  while(tC--){
    solve();
  }
}
```
