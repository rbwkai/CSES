# Permutations

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

A permutation of integers $1,2,\ldots,n$ is called beautiful if there are no adjacent elements whose difference is $1$.


Given $n$, construct a beautiful permutation if such a permutation exists.


## Input


The only input line contains an integer $n$.


## Output


Print a beautiful permutation of integers $1,2,\ldots,n$. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".


## Constraints


- $1 \le n \le 10^6$


## Example 1


Input:


```
5
```


Output:


```
4 2 5 3 1
```

## Example 2


Input:


```
3
```


Output:


```
NO SOLUTION
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

void solve(){
  ll n; cin>>n;
  if(n==1) {cout<<1<<endl; return;}
  if(n<4) {cout<<"NO SOLUTION"<<endl; return;}

  fir(n/2) cout<<2*(i+1)<<" ";
  fir((n+1)/2) cout<<2*i+1<<" ";
  cout<<endl;
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
