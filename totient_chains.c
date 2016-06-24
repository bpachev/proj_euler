#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define CAP 40000000
#define CHAIN_LEN 25


int * clens;
int * tots;

int cLen(int n)
{
  if (n == 1) return 1;
  
  if (clens[n] > 0) return clens[n];
  
  int temp = 1 + cLen(tots[n]);  
  clens[n] = temp;
  return temp; 
}

int main()
{
  tots = (int*)malloc(CAP*sizeof(int));
  char * mask = (char*)malloc(CAP);

  memset(mask,1,CAP);
  
  int i,j;
  
  for (i = 0; i < CAP; i++)
  {
    tots[i] = i;
  }
  
  	
  for (i = 2; i < CAP; i++)
  {
    if (mask[i])
    {
      tots[i]--;
      
      for (j = 2*i; j < CAP; j+=i)
      {
        mask[j] = 0;
        tots[j] -= tots[j]/i;
      }
    }
  }

  clens = (int*)malloc(CAP*sizeof(int));
  memset(clens,0,CAP*sizeof(int));
//  printf("phi(11) = %d\n",tots[11]);  
  unsigned long long int sum = 0;

  for (i = 2; i < CAP; i++)
  {
  //  printf("%d,%d, phi=%d\n",i,cLen(i),tots[i]);
    if (cLen(i) == CHAIN_LEN && mask[i]) sum += i; 
  }
  
  printf("Sum %llu\n",sum);
}

