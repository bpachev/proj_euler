#include "proj_euler.h"
#define CAP 100000000 
//#define CAP 30
#define NUMP 5761455

int * primes;

int pi(int n,int realNumPrimes)
{
  int pos = bin_search(primes,0,realNumPrimes-1,n);
  if (n<2) return 0;
//  printf("PI(%d) %d\n",n,pos);
  return pos;
}


int main()
{
  int i,j,s;
  s = 0;
  primes = (int*)malloc(NUMP*sizeof(int));
  char * mask = (char*)malloc(CAP);
  memset(mask,1,CAP);
  memset(primes,0,NUMP);
  int p = 0;
  
  for (i = 2; i < CAP; i++)
  {
    if (mask[i])
    {
      primes[p++] = i;
      
      if (CAP/i>=i)
      {
//        printf("Adding %d for %d\n",p,i);
        s += p;
      }
      
      else
      {
        s += pi(CAP/i,p);
      }  
      
      for (j=i+i;j<CAP;j+=i) mask[j] = 0;
    }
  }
  pi(0,p);
  printf("s = %d\n",s);
}
