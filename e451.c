#include "proj_euler.h"

#define CAP 20000000LL

int main()
{
  LL * I = (LL *)malloc((CAP+1)*sizeof(LL));
  LL i,j,s,t,d,sum;
  for (i = 0; i <= CAP; i++) I[i] = 1;
  
  for (i = 2; i <= CAP/2; i++)
  {
    for (j = 2; j <= CAP/i; j++)
    {
      LL k=1;
      d = EEA(i,j,&s,&t);
      if (d > 2)
      {
        continue;
      }
      
      if (d == 1)
      {
        k = (-2*s) % j;
        if (k < 0) k += j;
      }
      
      if (d == 2)
      {
        k = (-1*s) % j;
        if (k < 0) k += j;
        LL temp = (-1*(s+j/2)) % j;
        if (temp <0) temp += j;
        if (temp > k) k = temp;
      }
      
      if (k*i+1 > I[i*j] && k*i != i*j-2) 
      {
       I[i*j] = k*i+1;
//       printf("Changing I[%lld] to %lld\n",i*j,k*i+1);
      }
    }
  }
  
  sum = 0;
  
  for (i = 3; i <= CAP; i++)
  {
    sum += I[i];
  }
  
  printf("sum: %lld f(%lld)=%lld\n",sum,CAP,I[CAP]);
/*  LL s,t,a,b;
  s = t = 0;
  a = 5000LL;
  b = 22323LL;
  LL d = EEA(a,b,&s,&t); 
  printf("gcd(%lld,%lld) = %lld, s = %lld, t = %lld\n",a,b,d,s,t);
  printf("%lld %lld\n",s,t);*/
  
}
