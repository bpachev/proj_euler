#include "primes.h"
#define CAP 1000001
#define NUMP CAP/6

int amicable_chain(long long start,long long curr, int d);

int * chain_mask;
long long * div_mask;

int main()
{
  int max = 0;
  int min_elem = 0;
  char * mask = (char*)malloc(CAP/4); // because we only care about primes up to half the given cap
  unsigned long long int * primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  
  really_big_prime_mask_and_arr(mask,CAP/4,primes,NUMP);
  free(mask);
  div_mask = (long long*)malloc(CAP*sizeof(long long));
  chain_mask = (int*)malloc(CAP*sizeof(int));
  long int i,j,k;
  for (i = 0; i < CAP; i++) {div_mask[i] = 1; chain_mask[i] = -1;}
  
  for (i = 0; i < NUMP && primes[i] < CAP && primes[i]; i++)
  {
    unsigned long long int currp = primes[i];
    unsigned long long int cumup = currp;
    for (j = 0; cumup < CAP; j++)
    {
      long long mult = (cumup*currp - 1); 
      long long div = (j > 0) ? (cumup - 1) : currp - 1;
      for (k = cumup; k < CAP; k+=cumup)
      {
        if ( k == currp) continue;
        div_mask[k] *= mult;        
        div_mask[k] /=  div;
      }
      cumup *= currp;
    }
  }
  
  for (i = 2; i < CAP; i++) if(div_mask[i] > 1 + i) div_mask[i] -= i;
  
  //printf("div_mask[3] = %lld\n",div_mask[3]);
  
  for (i = 2; i < CAP; i++)
  {
//    printf("%ld\n",i);    
    if (chain_mask[i] == -1)
    {
      amicable_chain(i,i,0);
    }
    
    if (chain_mask[i] > max) 
    {
      max = chain_mask[i];
      min_elem = i;
    }
  }  
  
   
  printf("Smallest elem: %d with chain len %d\n",min_elem,max);
  free(div_mask);

}

int amicable_chain(long long start,long long curr, int d)
{
//  printf("%lld\n",curr);
  if (curr >= CAP || d > 30) return -1;
  if (chain_mask[curr] != -1 ) return chain_mask[curr]; 
  if (start == curr && d > 0) return d;
 
  if (curr == div_mask[curr]) return 0;
  int tmp = amicable_chain(start, div_mask[curr], d + 1);
  chain_mask[curr] = tmp;
  return tmp;
}
