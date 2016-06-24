#include "primes.h"

#define PCAP 1414
#define CAP 2000000

int is_squarefree(int k);

int * primes;
int * prime_squares;

int is_squarefree(int k)
{
  register int j;
  for (j = 0; j < PCAP; j++)
  {
    if (prime_squares[j] && k  % prime_squares[j] == 0) return 0;
  }
  
  return 1;
}


int main()
{
  register int i;
  char * mask = malloc(sqrt(CAP));
  primes = malloc(PCAP*sizeof(int));
  prime_squares = malloc(PCAP*sizeof(int));
  prime_mask_and_arr(mask, sqrt(CAP),primes, PCAP);
  for (i = 0; i < PCAP; i++)
  {
    prime_squares[i] = primes[i]*primes[i];
  }
  unsigned long long int sum = 1; // because 1 is squarefree 
  
  
  for (i = 2; i <= CAP;i++)
  {
    sum += is_squarefree(i);
    if (i % 100000 == 0) printf("There are %llu squarefree numbers under %d, ratio %f.\n " , sum, i,(float)sum/i);
  }
  printf("last prime %d\n",primes[PCAP-7]);
  
  printf("Sum: %llu\n",sum);
}