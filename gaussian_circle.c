#include "proj_euler.h"

// counts the number of gaussian integers with norm <= n
LL gaussian_circle(LL n)
{
  LL r = isqrt(n);
  LL res = 1 + 4*r;
//  LL n = r*r;
  for (LL i = 1; i <= r; i++)
  {
    res += 4*isqrt(n - i*i);
//    printf ("%llu\n",  isqrt(n - i*i));
  }
  return res;
}

LL cutoff(LL r, LL i, LL err)
{
   LL res = isqrt(err + 2*r*i - i*i);
//   printf ("cutoff(r = %llu, i = %llu) = %llu\n", r, i, res);
   return res;
}

LL fast_gaussian_circle(LL n)
{
//  printf("Called fast gaussian circle with %lld\n", n);
  LL r = isqrt(n);
  LL res= r;
  LL err = n - r*r;
  LL bound1 = isqrt(n/2);
  LL bound2 = isqrt(n - bound1*bound1);
  LL inc = bound2 * cutoff(r, r-bound2, err);
  LL last = r;
  for (LL i = 0; i < r - bound2; i++)
  {
  //  printf ("%lld\n",i);
    last = isqrt_init(err + 2*r*i - i*i, last);
//    if (last != isqrt(2*r*i - i*i)) printf("%lld, said %lld real %lld\n", 2*r*i - i*i, last, isqrt(2*r*i - i*i));
    inc += last;
    //inc += (r - i) * (cutoff(r, i) - cutoff(r, i-1));
  }

//  printf("inc %llu bound %llu, sum %llu\n", inc, bound1, 2*inc - bound1*bound1);
  return res +   (2*inc - bound1*bound1);
}


//#define CAP 100000000000000LL
#define CAP 100000000000000LL
LL cache_size;
LL * circle_cache;

LL gcircle(LL n)
{
//  printf("called with %lld returned %lld\n", n, fast_gaussian_circle(n));
  if (n < cache_size)
  {
    if (circle_cache[n]) return circle_cache[n];
    else
    {
        circle_cache[n] = fast_gaussian_circle(n);
        return circle_cache[n];
    }
  }

  return fast_gaussian_circle(n);
}


int main()
{
  cache_size = isqrt(CAP);
  circle_cache = big_arr(cache_size, 0);
  LL * mask = big_arr(cache_size+1, 3);
  LL tot = gcircle(CAP);
  for (LL p = 2; p <= cache_size; p++)
  {
    if (mask[p] == 3)
    {

      int power = 1;
      switch (p%4)
      {
        case 1:
        for (LL inc = p; inc <= cache_size; inc+=p)
        {
          int i = 0;
          LL temp = inc;
          while (temp %p == 0) {temp /= p; i++;}
          if (mask[inc] ==3) mask[inc] =1;
          if (i == 1) {
             mask[inc] = -2 * mask[inc];
          }
          else if (i == 2) mask[inc] == -mask[inc];
          else mask[inc] =0;
        }
        break;
        case 3:
        power = 2;
        case 2:
        for (LL inc = p; inc <= cache_size; inc+=p)
        {
          int i = 0;
          LL temp = inc;
          while (temp %p == 0) {temp /= p; i++;}
          if (i == power) {
            if (mask[inc] ==3) mask[inc] =1;
             mask[inc] = -mask[inc];}
          else mask[inc] =0;
        }
      }
    }

    if (mask[p] != 0)
    {
      tot += mask[p]*gcircle(CAP/p/p);
    }
//    printf("mask[%lld] = %lld\n", p, mask[p]);
  }
 printf("total %lld\n", tot);
  free(mask);
}
