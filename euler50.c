#include "primes.h"
#define CAP 1000000
#define SUM_CAP 1000

int main()
{
  char * mask = (char*)malloc(CAP);
  int * primes = (int *)malloc(sizeof(int)*P_UNDER_MILLION);
  int psums[SUM_CAP];
  int i,j;  
  unsigned long long int sum = 0;
  int longest_chain = 0;
  long int prime_sum = 0;
  
  
  prime_mask_and_arr(mask, CAP, primes, P_UNDER_MILLION);
  for (j = 0; j < SUM_CAP; j++)
  {
    sum = 0;
    for (i = j; i < 2*SUM_CAP; i++) 
    {
      if (j == 0) 
      {
        sum += primes[i];
        if(i<SUM_CAP) psums[i] = sum;
        else printf("cap too small %d\n",i);
      }
      
      else
      {
        if(j-1<SUM_CAP&&i<SUM_CAP) sum = psums[i] - psums[j-1];
        else sum += primes[i];
      }
      
      if (sum >= CAP) break;
      if (MASK_WITH_CHECK(sum,mask))
      {
        if (i+1-j > longest_chain)
        {
          longest_chain = i+1-j;
          prime_sum = sum;
        }
      }
    }
  } 
    printf("%ld is prime, sum of %d primes\n",prime_sum,longest_chain);  
}
