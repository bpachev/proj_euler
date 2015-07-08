#include "primes.h"
#define CAP 1125899906842624
#define NUMP 33554432 //2^25
#define PCAP 2063689 // primes less than 2^25
#define MAX_PS 9

unsigned long long int * primes;
unsigned long long int * prime_squares;
char * p_div_mask;
unsigned long long int  p_divs[MAX_PS];

unsigned long long int squarefree(unsigned long long int n, unsigned long long int div_cap);
unsigned long long int mod_squarefree(unsigned long long int n, unsigned long long int div_cap);


unsigned long long int squarefree(unsigned long long int n, unsigned long long int div_cap)
{
  unsigned long long int dec = 0;
  unsigned long long int i = 0;
  unsigned long long int real_cap = (n < div_cap ) ? n + 1: div_cap; 
  while (i < PCAP && prime_squares[i] < real_cap && prime_squares[i])  {
    dec += squarefree(n/prime_squares[i],prime_squares[i]);
    i++;
  }  
  return n - dec;
}

unsigned long long int mod_squarefree(unsigned long long int n, unsigned long long int div_cap)
{
  unsigned long long int dec = 0;
  unsigned long long int i = 0;
  int j = 0;
  unsigned long long int real_cap = (n < div_cap ) ? n + 1: div_cap;
  while (j < MAX_PS && p_divs[j] < prime_squares[i] && p_divs[j] < real_cap && p_divs[j])
  {
    dec += squarefree(n/p_divs[j],p_divs[j]);
    j++;
  }
  
  while (i < NUMP && prime_squares[i] < real_cap && prime_squares[i])  {
    while (j < MAX_PS && p_divs[j] < prime_squares[i] && p_divs[j])
    {
      dec += squarefree(n/p_divs[j],p_divs[j]);
      j++;
    }
    if(!p_div_mask[i]) dec += squarefree(n/prime_squares[i],prime_squares[i]);
    i++;
  }
  
  while (j < MAX_PS && p_divs[j] < prime_squares[i] && p_divs[j] < real_cap && p_divs[j])
  {
    dec += squarefree(n/p_divs[j],p_divs[j]);
    j++;
  }

  
  return n - dec;
}



int main()
{
  p_div_mask = (char *)malloc(NUMP);
  memset(p_divs, 0, sizeof(p_divs));
  memset(p_div_mask, 0, NUMP);  
  primes = malloc(sizeof(unsigned long long int)*PCAP);
  prime_squares = malloc(sizeof(unsigned long long int)*PCAP);
  char * mask = malloc(sqrt(CAP)); 
  really_big_prime_mask_and_arr(mask, sqrt(CAP), primes, PCAP);
  free(mask);
  unsigned long long int i;
  for (i = 0; i < PCAP; i++)
  {
    prime_squares[i] = primes[i]*primes[i];
  }
  
  printf("There are %llu squarefree numbers under 20^50\n",mod_squarefree(CAP,CAP));

}
