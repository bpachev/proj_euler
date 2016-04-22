#include "proj_euler.h"

// counts the number of gaussian integers with norm <= n
LL gaussian_circle(LL r)
{
  LL res = 1 + 4*r;
  LL n = r*r;
  for (LL i = 1; i < r; i++)
  {
    res += 4*isqrt(n - i*i);
//    printf ("%llu\n",  isqrt(n - i*i));
  }
  return res;
}

LL cutoff(LL r, LL i)
{
   LL res = isqrt(2*r*i - i*i);
//   printf ("cutoff(r = %llu, i = %llu) = %llu\n", r, i, res);
   return res;
}

LL fast_gaussian_circle(LL r)
{
  LL res= 1 + 4*r;
  LL n = r*r;
  LL bound1 = isqrt(n/2);
  LL bound2 = isqrt(r*r - bound1*bound1);
  LL inc = bound2 * cutoff(r, r-bound2);
  LL last = r;
  for (LL i = 1; i < r - bound2; i++)
  {
    last = isqrt_init(2*r*i - i*i, last);
//    if (last != isqrt(2*r*i - i*i)) printf("%lld, said %lld real %lld\n", 2*r*i - i*i, last, isqrt(2*r*i - i*i));
    inc += last;
    //inc += (r - i) * (cutoff(r, i) - cutoff(r, i-1));
  }

  //printf("inc %llu bound %llu, sum %llu\n", inc, bound1, 2*inc - bound1*bound1);
  return res +  4 * (2*inc - bound1*bound1);
}

#define CAP 100000000000000LL

int main()
{
//  for (LL i =0;i < 1000; i++) printf("%lld ",gaussian_circle(i)-fast_gaussian_circle(i));
  LL n = 10000000;
  //printf("real %llu\n", gaussian_circle(n));
  printf("fast %llu\n", fast_gaussian_circle(n));
//  for (int i=0; i < n ; i++) if (isqrt_init(n, i+1) != isqrt(n)) printf("uh-oh %d",i);
//  printf("sqrt(%lld) = %lld", n, isqrt_init(n, (n+1)/2));
}
