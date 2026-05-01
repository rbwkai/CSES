# Labyrinth

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given a map of a labyrinth, and your task is to find a path from start to end. You can walk left, right, up and down.


## Input


The first input line has two integers $n$ and $m$: the height and width of the map.


Then there are $n$ lines of $m$ characters describing the labyrinth. Each character is . (floor), # (wall), A (start), or B (end). There is exactly one A and one B in the input.


## Output


First print "YES", if there is a path, and "NO" otherwise.


If there is a path, print the length of the shortest such path and its description as a string consisting of characters L (left), R (right), U (up), and D (down). You can print any valid solution.


## Constraints


- $1 \le n,m \le 1000$


## Example


Input:


```
5 8
########
#.A#...#
#.##.#B#
#......#
########
```


Output:


```
YES
9
LDDRRRRRU
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


void solve(){
  ll n, m; cin>>n>>m;
  string s, t; fir(n) cin>>t, s+=t;
  ll sr, ds; fir(n*m){
    if(s[i]=='A') ds=i;
    if(s[i]=='B') sr=i, s[sr]='#';
  }

  vi del(n*m, 0);
  vi depth(n*m, -1);
  queue<ll> qu; qu.push(sr);
  map<ll, char> mp={{1, 'R'}, {-1, 'L'}, {m, 'D'}, {-m, 'U'}};
  ll d=0, cl=1, nl=0;
  while(sz(qu)){
    ll id=qu.front(); qu.pop(); depth[id]=d; cl--;
    
    if(id==ds) break;

    if(id%m != 0 and s[id-1]!='#') qu.push(id-1), s[id-1]='#', del[id-1]=1, nl++;
    if(id/m != 0 and s[id-m]!='#') qu.push(id-m), s[id-m]='#', del[id-m]=m, nl++; 

    if(id%m != m-1 and s[id+1]!='#') qu.push(id+1), s[id+1]='#', del[id+1]=-1, nl++;
    if(id/m != n-1 and s[id+m]!='#') qu.push(id+m), s[id+m]='#', del[id+m]=-m, nl++;

    if(!cl) d++, cl=nl, nl=0;
  }

  if(!del[ds]) cout<<"NO"<<en;
  else{
    cout<<"YES"<<en<<depth[ds]<<en;
    while(ds!=sr){
      cout<<mp[del[ds]];
      ds+=del[ds];
    }
    cout<<en;
  }
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
