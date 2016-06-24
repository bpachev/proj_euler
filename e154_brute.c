#include "proj_euler.h"
#define N 200000LL

int main()
{
 LL x,y;
 LL count = 0;
 LL Nord5 = pfact_ord(N,5LL);
 LL Nord2 = pfact_ord(N,2LL);
 LL* ords_5 = big_arr(N+1,0);
 LL* ords_2 = big_arr(N+1,0);
 
 int i;
 for (i=0; i<=N;i++)
 {
  LL t = i;
  ords_5[i] = pfact_ord(t,5LL);
  ords_2[i] = pfact_ord(t,2LL);
 }
 
 for (x = 1LL;x<N;x++)
 {
  if (Nord5-ords_5[x]-ords_5[N-x] >= 5)
  {
   for (y = 0LL; y <= N-x; y++)
   {
    if (Nord5-ords_5[x]-ords_5[y]-ords_5[N-y-x] >= 12 && Nord2-ords_2[x]-ords_2[y]-ords_2[N-y-x]>=12)
    {
     count++;
    }
   }
  }
 }
 printf("Number of trinomial coefficients with top %llu divisible by 10^12 %llu\n",N,count); 
}
