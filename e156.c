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
 // printf("%lld %lld %lld\n",res,fp10[curr_exp],mod);
  mod += curr_d*p10[curr_exp];
  curr_exp++;
 }
 return res;
}

LL search(LL a,LL b,LL fa,LL fb,LL d)
{
 if (b-a<2) return 0;
 if (fa>b||a>fb) return 0;
 LL mid = (a+b)/2;
 LL fmid = f(mid,d);
 LL res = 0;
 if (mid == fmid) {res = mid; printf("found %llu\n",mid);}
 return mid + search(a,mid,fa,fmid,d) + search(mid,b,fmid,fb,d);
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
 printf("search(0,10000000)=%llu\n",search(0,p10[11],0,fp10[11],1LL));
}
