#include "proj_euler.h"
#define CAP 1000000

int main()
{
  int * mask = (int*)malloc(sizeof(int)*CAP);
  
  int i,j;
  LL s = 0;
  for (i = 0; i < CAP; i++)
  {
    mask[i] = digit_root(i);
 //   printf("%d %d\n",mask[i],i);
  }
  
  for (i = 2; i < CAP; i++)
  {
    s = s + mask[i];
//    printf("mask[%d] %d\n",i,mask[i]);
    for (j = 2; j <= i && j*i < CAP; j++)
    {
      int t = mask[i]+mask[j];
      if (t > mask[i*j])
      {
        mask[i*j] = t;
      }
    }
  }
//  printf("mask[24] %d\n",mask[24]);
  printf("sum %lld\n",s);
}
