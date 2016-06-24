#include "proj_euler.h"
#define CAP 50000000
#define NUM_SOLS 1

int main()
{
  int * mask = (int*)malloc(CAP*sizeof(int));
  memset(mask,0,CAP*sizeof(int));
  printf("no memory trouble\n"); 
  int i,y,k;
  int s = 0;
  
  for (y = 2; y < CAP; y++)
  {
    for (k = (y >> 2) + 1; y*(4*k-y) < CAP && k < y; k++)
    {
      mask[y*(4*k-y)] += 1;
    }
  }
  
  for (i = 1; i < CAP; i++)
  {
    if (mask[i] == NUM_SOLS)
    {
      s++;
    }
  }
  
  printf("%d values of n less than %d have exactly %d sols\n",s,CAP,NUM_SOLS);
}
