#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#define POW_CAP 10
#define NUM_URNS 7
#define NUM_BALLS 20

int main()
{
  int i;
  int num_d[POW_CAP+1];
  int fact[NUM_URNS+1];  
  memset(num_d,0,sizeof(num_d));
  long int sum = 0;
  long int cum_val = 0;
  int counter = NUM_URNS;
  fact[0] = 1;
  for (i = 1; i <= NUM_URNS; i++)
  {
    fact[i] = i*fact[i-1];
  }
  while(1)
  {
    for (i = 0; i <= POW_CAP; i++)
    {
      if (counter)
      {
        num_d[i]++;
        counter--;
        break;
      }
      else
      {
        counter += num_d[i];
        num_d[i] = 0;
      }
    }
    long int prod = fact[NUM_URNS];
    register int balls = 0;
    for (i = 0; i <= POW_CAP; i++) balls += i*num_d[i];
    
    if (balls == NUM_BALLS && !counter)
    {
      for (i = 0; i <= POW_CAP; i++) 
      {
       // printf("%d %d, ",i,num_d[i]);
        prod /= fact[num_d[i]];
      }
      //printf("\n");
      cum_val += prod*(NUM_URNS-num_d[0]);
      sum += prod;
    }
    
    if (num_d[POW_CAP] == NUM_URNS) break;
  }
  printf("There are %ld possible combinations, cum_val %ld.\n",sum,cum_val);
}