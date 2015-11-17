#include "proj_euler.h"
#define MAXPOW 11 
//MAXPOW is the maximum power of 10 considered
LL p10[MAXPOW+1];
LL fp10[MAXPOW+1];

LL f(LL n, LL d)
{
 LL res = 0;
 LL curr_exp = 0;
 LL curr_d;
 LL mod = 0;
 
 while (n)
 {
  curr_d = n%10;
  n /= 10;
  if (curr_d>d) res += p10[curr_exp];  
  else if (curr_d==d) res += (mod+1);
  res += curr_d*fp10[curr_exp];
  mod = 10*mod+curr_d;
  curr_exp++;
 }
 return res;
}

int main()
{
 int i;
 p10[0] = 1;
 fp10[0] = 0;
 for (i=1;i<MAXPOW;i++)
 {
  p10[i] = 10*p10[i-1];
  fp10[i] = i*p10[i-1];
 }
 printf("f(%llu,1)=%llu\n",199981LL,f(199981LL,1LL));
}
