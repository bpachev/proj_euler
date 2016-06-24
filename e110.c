#include "primes.h"
#define SOL_CAP 4000000
#define PCAP 1000
#define NUMP 20
#define POW_CAP 3
#define TOL SOL_CAP/7

unsigned long long int ipow(unsigned long long int base, unsigned long long int exp);


unsigned long long int ipow(unsigned long long int base, unsigned long long int exp)
{
    unsigned long long int result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

int main()
{
  int num_d[POW_CAP+1];
  unsigned long long int min = ((unsigned long long int)2) << 60;
  char * mask = (char*)malloc(PCAP);
  int * primes = (int*)malloc(PCAP/5*sizeof(int));
  prime_mask_and_arr(mask,PCAP,primes,PCAP/5);
  memset(num_d, 0, sizeof(num_d));
  register int counter = NUMP;
  register int i;
  
  while(1)
  {
    unsigned long long int prod = 1;
    for (i = 1; i <= POW_CAP; i++)
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
    
    for (i = 1; i <= POW_CAP; i++) prod *= ipow(2*i + 1,num_d[i]);
    prod = prod/2 +1;
    if (prod > SOL_CAP && prod < SOL_CAP + TOL)
    {
      unsigned long long int tmp = 1;
      register int curr_prime_index = 0;
      register int j;
      for (i = POW_CAP; i >= 1; i--)
      {
        for (j = 0; j < num_d[i]; j++) 
        {
          tmp *= ipow(primes[curr_prime_index++],i); 
        }
      }
      
      if (tmp < min) {min = tmp;}
    }
    if (num_d[POW_CAP] == NUMP)
    {
      break;
    } 
  }
  printf("min %llu\n",min);
}