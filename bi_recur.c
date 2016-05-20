#include "proj_euler.h"


LL mod = 1L << 60L;

LL max(LL a, LL b);
LL min(LL a, LL b);
LL x_k(LL k);
LL half_A(LL n,LL k, LL lower, LL upper);
LL A(LL n, LL k, LL lower , LL upper);


LL max(LL a, LL b)
{
  if (a > b) return a;
  else return b;
}

LL min(LL a, LL b)
{
  if (a > b) return b;
  else return a;
}

LL x_k(LL k) {
  if (k <= 1)  return k;
  LL k_coeff = 1;
  LL k2_coeff = 0;
  while (k != 1){
    if (k % 2)
    {
      LL temp = k_coeff;
      k_coeff = (k2_coeff + 2*k_coeff) % mod;
      k2_coeff = (3*temp) % mod;
    }
    else {
      LL temp = k_coeff;
      k_coeff = (k2_coeff + 3*k_coeff) % mod;
      k2_coeff = (2*temp) % mod;
    }
    k = k / 2;
  }
  return k_coeff % mod;
}

LL half_A(LL n,LL k, LL lower, LL upper){
    LL res = A(n, 2*k, lower, upper);
    if (res <= upper) res = max(res, A(n, 2*k+1, max(lower, res), upper));
    return res;
}

LL A(LL n, LL k, LL lower , LL upper)
{
    if (k >= n) return x_k(k);
    else if (k >= (n-1) / 2) return mod - 1 - max(A(n, 2*k, lower, upper), A(n, 2*k+1, lower, upper));
    else {
        LL first = half_A(n, 2*k, lower, upper);
        if (first >= lower) first = min(first, half_A(n, 2*k+1, lower, min(upper, first)));
        return first;
    }
}

int main()
{
  LL n = 1000000000000;
  printf("A(%lld) = %lld\n", n, A(n, 1 , 0, mod));
}
