#include "primes.h"

#define CAP 1000000

int num_primes_generated(int a, int b, char* mask, int c);

int main()
{
  char* mask = (char *)malloc(CAP);
  int* primes = (int *)malloc(P_UNDER_1000);
  memset(primes,0,sizeof(primes));
  prime_mask_and_arr(mask, CAP,primes, P_UNDER_1000);
  int i = 0;
  int j = 0;
  int mprimes = 0;
  int ma = 0;
  int mb = 0;
  int curr = 0;  
  
  for (i = 0;i < P_UNDER_1000; i++)
  {
    for (j = 0; j < P_UNDER_1000; j++)
    {
  //    printf("on iter i = %d, j= %d.\n", i,P_UNDER_1000);
      int pj = primes[j];
      int pi = primes[i];
      curr = num_primes_generated(pi,pj, mask, CAP);

      if (curr > mprimes) 
      {
        mprimes = curr;
        ma = pi;
        mb = pj;
      }
      
      curr = num_primes_generated(-pi,pj, mask, CAP);

      if (curr > mprimes) 
      {
        mprimes = curr;
        ma = -pi;
        mb = pj;
      }
      
    }
  }
  
  printf("Best Quadratic primes equation n^2 + %dn + %d prod: %d.\nProduces %d primes.\n",ma,mb,ma*mb,mprimes);
}

int num_primes_generated(int a, int b, char* mask, int c)
{
  int n = 0;
  while(1)
  {
    long int q = n*n + a*n + b;
    if (q % 2 == 0 || q < 2) return n;        
    
    long int temp = CONV_TO_MASK(q);
    if (temp < c)
    {
      if (!mask[temp]) return n;
    }
    
    else
    {
      if (!slow_prime_check(n)) return n; 
    }
    
    n++;
  }
}

