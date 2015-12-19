#include "stdio.h"
#include "stdlib.h"
#include "string.h"
typedef long long int LL;
#define N 200000LL

//the order of a prime in a factorial
LL pfact_ord(LL n,LL p)
{
 LL res = 0;
 while (n)
 {
  n/=p;
  res += n;
 }
 return res;
}

int main()
{
 LL i;
 LL n_ops=0;
 LL ord_top = pfact_ord(N,5LL);
 for (i=1;i<N;i++)
 {
  LL o1 = pfact_ord(i,5LL);
  LL o2 = pfact_ord(N-i,5LL);
  if (ord_top-o1-o2 >= 5)
  {
   n_ops += N-i;
  }
 }
 printf("Num operations currently needed: %llu\n",n_ops);
}
