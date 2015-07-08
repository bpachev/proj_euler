#include <stdio.h>
#include <stdlib.h>
typedef long long int LL;

long long int isqrt(long long int n)
{
    long long int x = n;
    long long int y = (x + 1) / 2;
    while (y < x)
    {
        x = y;
        y = (x + n / x) / 2;
    }
    return x;
}

LL count_medians(LL n)
{
 LL res = 0;
 LL p,s,k,t;
 for (p = 1; p*p < n; p++) {
  for (s = 1; s*s < n; s++)  {
  for (t = 1; 2*t*s*p  + 2*t*t*s*s < n && t*t<n; t++)  {
  for (k = 1; k <= t; k++)  { 
   LL tk = t+k;
   LL x = p*p + 2*tk*p*s - (t-k)*(t-k)*s*s;
   LL y = 2*tk*p*s + 2*tk*tk;
   LL z = p*p + 2*tk*p*s + (3*t*t+6*t*k-k*k)*s*s;
   LL r = p*p + 2*tk*p*s + (3*k*k+6*k-t*t)*s*s;
   if (x > n || y > n || z > n) break;
   if (!(2*x*x+2*y*y==z*z+r*r))
   {
     printf("FAILS for %lld %lld %lld %lld\n",x,y,z,r);
   }
   else
   {
     res++;
   }
  }
  }
  }
 }
 return res; 
}

int main()
{
  long long int max_c = 20;
  long long int a,b,c,sum;
  sum = 0;
  for (c = 1; c <= max_c; c++) {
    for (b = c/2; b <= c; b++)
    {
      for (a = c - b + 1; a <= b; a++)
      {
        long long int temp = 2*(a*a + b*b) - c *c;
        long long int sq = isqrt(temp);
        if (sq*sq == temp && sq % 2 == 0) {
         sum++;
//         printf("sq: %lld, temp %lld, (a,b,c) = (%lld,%lld,%lld) %lld\n",sq,temp,a,b,c,2*(a*a + b*b));
         }
      }
    }
  }
  printf("Number of admissible triangles %lld\n",sum);
  printf("cm(%lld) %lld\n",max_c,count_medians(max_c));
}
