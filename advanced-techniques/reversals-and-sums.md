# Reversals and Sums

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given an array of $n$ integers, you have to process following operations:



reverse a subarray
calculate the sum of values in a subarray

## Input


The first input line has two integers $n$ and $m$: the size of the array and the number of operations. The array elements are numbered $1,2,\dots,n$.


The next line as $n$ integers $x_1,x_2,\dots,x_n$: the contents of the array.


Finally, there are $m$ lines that describe the operations. Each line has three integers $t$, $a$ and $b$. If $t=1$, you should reverse a subarray from $a$ to $b$. If $t=2$, you should calculate the sum of values from $a$ to $b$.


## Output


Print the answer to each operation where $t=2$.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le m \le 10^5$
- $0 \le x_i \le 10^9$
- $1 \le a \le b \le n$


## Example


Input:


```
8 3
2 1 3 4 5 3 4 4
2 2 4
1 3 6
2 2 4
```


Output:


```
8
9
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
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

static mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
static uniform_int_distribution<int> rndm(1, (int)2e9);

template<typename T>
struct Node{
  T val, res;
  ll pri, sze;
  bool rev;
  Node *l, *r;
  
  Node(const T& v): val(v), res(v),
                    pri(rndm(rng)),
                    sze(1),
                    rev(false),
                    l(nullptr), r(nullptr) {}
};

template<typename T>
int size(Node<T>* t){ return t? t->sze: 0; }

template<typename T>
T rslt(Node<T>* t){ return t? t->res: 0; } //result identity

template<typename T>
void pull(Node<T>* t){
  if(!t) return;
  t->res = t->val + rslt(t->l)+rslt(t->r);
  t->sze = 1 + size(t->l)+size(t->r);
}

template<typename T>
void push(Node<T>* t){
  if(!t or !t->rev) return;
  t->rev = false;

  swap(t->l, t->r);
  if(t->l) t->l->rev ^= true;
  if(t->r) t->r->rev ^= true;
}

template<typename T>
Node<T>* merge(Node<T>* L, Node<T>* R){
  if(!L) return R;
  if(!R) return L;

  push(L); push(R);
  if(L->pri > R->pri){
    L->r = merge(L->r, R);
    pull(L); return L;
  }else{
    R->l = merge(L, R->l);
    pull(R); return R;
  }
}

template<typename T>
pair<Node<T>*, Node<T>*> split(Node<T>* t, int k){
  if(!t) return {nullptr, nullptr};
  push(t);

  if(size(t->l) >= k){
    auto pr = split(t->l, k);
    t->l = pr.second;
    pull(t); return {pr.first, t};
  }else{
    auto pr = split(t->r, k-size(t->l)-1);
    t->r = pr.first;
    pull(t); return {t, pr.second};
  }
}

template<typename T>
Node<T>* reverse(Node<T>* t){
  t->rev ^= true;
  return t;
}

template<typename T>
Node<T>* build(vector<T> &v){
  Node<T>* tree = nullptr;
  fir(sz(v)){
    Node<T>* cur = new Node(v[i]);
    tree = merge(tree, cur);
  }
  return tree;
}
template<typename T>
void destroy(Node<T>* t){
  if(!t) return;
  destroy(t->l); destroy(t->r);
  delete t;
}

template<typename T>
void print(Node<T>* t) {
  if(!t) return;
  push(t);

  print(t->l);
  cout<<t->val;
  print(t->r);
}

void solve(){
  ll n, k; cin>>n>>k;
  vi v(n); fir(n) cin>>v[i];

  auto tree = build(v);
  fir(k){
    ll t, l, r; cin>>t>>l>>r; l--; r--;
    if(t==1){
      auto [A, B] = split(tree, l);
      auto [Bp, C] = split(B, r-l+1);

      B = reverse(Bp);
      tree = merge(A, merge(B, C));
    }
    if(t==2){
      auto [A, B] = split(tree, l);
      auto [Bp, C] = split(B, r-l+1);

      cout<<rslt(Bp)<<en;
      tree = merge(A, merge(Bp, C));
    }
  }
  destroy(tree);
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
