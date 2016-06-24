#include "proj_euler.h"
#define CAP 10000000000LL


int main()
{
 double ans = 1.;
 LL i  = CAP;
 LL j;
 for (j = 2; j <= CAP; j++)
 {
   double t1 = 1./j;
   double t2 = t1/j;
   ans = t1+t1 - t2 + (1-t2) * ans;
 }
 printf("R(%lld) = %.12f\n",CAP,ans);
}
