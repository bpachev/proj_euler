#include "proj_euler.h"
#define N 1000000000000000
#define NEXT(x,mod) (3+x*(10 + 6 * x)) % mod

int cycle_len(LL mod)
{
 LL tort = NEXT(1,mod);
 LL hare = NEXT(tort,mod);
 int i = 1;
 while (tort != hare)
 {
   tort = NEXT(tort,mod);
   hare = NEXT(hare,mod);
   hare = NEXT(hare,mod);
   i += 1;
 }
 return i;
}

LL eval(LL x, int mod,LL n)
{
  int i;
  for (i=0;i<n;i++)
  {
    x = NEXT(x,mod);
  }
  return x;
}

int main()
{
  LL i;
  LL test = 1000000009LL;
  for (i=0;i<100;i++) {
   LL c = cycle_len(test+i);
   printf("f(%lld) %lld\n",test+i,eval(1,test+i,N%c));
 }
}
