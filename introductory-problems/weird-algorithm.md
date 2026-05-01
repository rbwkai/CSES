# Weird Algorithm

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider an algorithm that takes as input a positive integer $n$. If $n$ is even, the algorithm divides it by two, and if $n$ is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until $n$ is one. For example, the sequence for $n=3$ is as follows:


$$
3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1
$$


Your task is to simulate the execution of the algorithm for a given value of $n$.


## Input


The only input line contains an integer $n$.


## Output


Print a line that contains all values of $n$ during the algorithm.


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
3
```


Output:


```
3 10 5 16 8 4 2 1
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
  while(n-1){
    cout<<n<<" ";
    if(n%2) n= 3*n +1;
    else n/=2;
  }
  cout<<1<<endl;
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
