#include "primes.h"
#include "stdarg.h"
#define CAP 3000000000
#define NP sqrt(CAP)/6

void die(const char* msg, ...);


int main()
{
  unsigned long long int i;
  unsigned long long int k = 0;
  unsigned long long int num_diagonal = 1;
  unsigned long long int nump = 0;

  char * mask = (char*)malloc(sqrt(CAP)/2);
  if (!mask) die("Could not allocate memory for mask");
  unsigned long long int * primes = (unsigned long long int*)malloc(sizeof(unsigned long long int)*NP);
  if (!primes) die("Could not allocate memory for primes");
  really_big_prime_mask_and_arr(mask, sqrt(CAP)/2,primes, NP);
  
  for (i = 1; k*k < CAP; i++)
  {
    num_diagonal += 4;
    k = 2*i + 1;
    nump += big_faster_prime_check(k*k-2*i,primes,NP) + big_faster_prime_check(k*k-4*i,primes,NP) + big_faster_prime_check(k*k-6*i,primes,NP);
    if (nump*10 < num_diagonal) break;
  }
  
  printf("%llu out of %llu diagonal elements are prime\nside length %llu",nump,num_diagonal,i*2+1);
}


void die(const char* msg, ...)
{
  va_list ap;
  va_start(ap,msg);
  
  fprintf(stderr, "fatal_error: ");
  vfprintf(stderr, msg, ap);
  va_end(ap);
  fputc('\n',stderr);
  exit(1);
}
