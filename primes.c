#include "primes.h"



//computes tot[n] for all odd n

void tot_fill(char* mask, int c,int * tot)
{
  memset (mask,1,c);
  int i;
  for (i=0;i<c;i++)
  {
    tot[i] = 1 + 2*(i+1);
  }

  for (i=0;i<c;i++)
  {
    int inc = 1 + 2*(i+1);
    if (mask[i] == 1)
    {
      int j;
      tot[i]--; //tot(p) = p-1 for p prime.
      for (j = i+inc;j<c;)
      {
        mask[j] = 0;
        tot[j] = tot[j] - (tot[j] / inc);
        j += inc;
      } 
    }
  }
}





//mask becomes a mask of the primality of all odd numbers >=3 and <= 2*cap 

void prime_mask(char* mask, int c)
{
  memset (mask,1,c);
  int i;
  for (i=0;i<c;i++)
  {
    if (mask[i] == 1)
    {
      int inc = 1 + 2*(i+1);
      int j;
      for (j = i+inc;j<c;)
      {
        mask[j] = 0;
        j += inc;
      } 
    }
  }
}


void big_prime_mask(char* mask, unsigned long long int c) 
{
  memset (mask,1,c);
  unsigned long long int i;
  for (i=0;i<c;i++)
  {
    if (mask[i] == 1)
    {
      unsigned long long int inc = 1 + 2*(i+1);
      unsigned long long int j;
      for (j = CONV_TO_MASK(inc*inc);j<c;)
      {
        mask[j] = 0;
        j += inc;
      } 
    }
  }
}


//similar to the first function, except it also returns an array containing actual primes.
//Note that if there are not nump primes less than c, 

void prime_mask_and_arr(char* mask, int c,int* primes, int nump)
{
  memset (mask,1,c);
  int i;
  int p = 1;
  primes[0] = 2;
  for (i=0;i<c;i++)
  {
    if (mask[i] == 1)
    {
      int inc = 1 + 2*(i+1);
      if (p < nump) primes[p++] = inc;
//      printf("inc: %d p: %d np %d\n", inc,p,nump);      
      int j;
      for (j = i+inc;j<c;)
      {
        mask[j] = 0;
        j += inc;
      } 
    }
  }
//  printf("fooo%d\n",primes[1]);
  
}

void big_prime_mask_and_arr(char* mask, int c, long int* primes, int nump)
{
  memset (mask,1,c);
  memset (primes,0,sizeof(long int)*nump);
  int i;
  int p = 1;
  primes[0] = 2;
  for (i=0;i<c;i++)
  {
    if (mask[i] == 1)
    {
      long int inc = 1 + 2*(i+1);
//      printf("inc: %d p: %d\n", inc,p);
      if (p < nump) primes[p++] = inc;
      int j;
      for (j = CONV_TO_MASK(inc*inc);j<c;)
      {
        mask[j] = 0;
        j += inc;
      } 
    }
  }
}

void really_big_prime_mask_and_arr(char* mask, unsigned long long int c, unsigned long long int* primes, unsigned long long int nump)
{
  memset (mask,1,c);
  memset (primes,0,sizeof(unsigned long long int)*nump);
  unsigned long long int i;
  unsigned long long int p = 1;
  
  for (i = 0; i < nump; i++) primes[i] = 0;
  primes[0] = 2;
  for (i=0;i<c;i++)
  {
    if (mask[i] == 1)
    {
      unsigned long long int inc = 1 + 2*(i+1);
//      printf("inc: %d p: %d\n", inc,p);
      if (p < nump) primes[p++] = inc;
      unsigned long long int j;
      for (j = CONV_TO_MASK(inc*inc);j<c;)
      {
        mask[j] = 0;
        j += inc;
      } 
    }
  }
}


int faster_prime_check(long int n, int* primes, int nump)
{
  int curr_div = 1;
  int i = 0;
  
  while (curr_div < sqrt(n))
  {
    if (i < nump) curr_div = primes[i++];
    else curr_div++;
 //   printf("%d nump %d curr_div, %ld n\n",nump,primes[1],n);
    
    if (n % curr_div == 0) return 0;
  }
  
  return 1;
}

int big_faster_prime_check(unsigned long long int n, unsigned long long int* primes, unsigned long long int nump)
{
  unsigned long long int curr_div = 1;
  unsigned long long int i = 0;
  
  while (curr_div < sqrt(n))
  {
    if (i < nump) curr_div = primes[i++];
    else curr_div++;
 //   printf("%d nump %d curr_div, %ld n\n",nump,primes[1],n);
    
    if (n % curr_div == 0) return 0;
  }
  
  return 1;
}


int slow_prime_check(long int n)
{
  int i;
  for (i = 2; i < (int)sqrt(n); i++)
  {
    if(n % i == 0) return 0; 
  }
  
  return 1;
}
