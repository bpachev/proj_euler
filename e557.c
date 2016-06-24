#include "proj_euler.h"
#include "math.h"

LL triangle_cuts(LL n)
{
  LL A, a;
  LL result = 0;
  for (A = 4; A <= n; A++) {
    for (a = 1; a <= n-3; a++) {
      LL p, q, g, num, denom;
      num = a*a;
      denom = A+a;
      g = big_gcd(num, denom);
      p = num/g;
      q = denom/g;
      LL k;
      for (k = 1; k <= (A-a)/q; k++) {
        LL prod, sum;
        prod = p*k;
        sum = A - a - q*k;
        LL disc = sum*sum - 4 * prod;
        if (disc < 0) break;
        LL sq = sqrt(disc);
        if (sq*sq == disc) {
          result += A;
        }
      }
    }
  }
  return result;
}

int main()
{
  LL n = 10000;
  printf("S(%lld) = %lld.\n", n, triangle_cuts(n));
}
