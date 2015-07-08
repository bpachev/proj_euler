#include "proj_euler.h"

#define NUM 20000000
#define D1 5000000
#define D2 15000000


int main()
{
  ULL i,j;
  char * mask = (char*)malloc(NUM);
  
  memset(mask,1,NUM);
  
  ULL s = 0; 
  for (i = 2; i < NUM; i++)
  {
    if (mask[i])
    {
      ULL accum = i;
      
      while (accum < NUM)
      {
        s += i * (NUM/accum - D1/accum - D2/accum);
        accum *= i;
      }
      
      for (j = i*i; j < NUM; j += i)
      {
        mask[j] = 0;
      }
    }
  }
  
  printf("sum: %llu\n",s);
}
