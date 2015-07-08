#include "primes.h"
//#define CAP (5000000000000000LL)
#define CAP 102*102
#define TST_CAP CAP
#define NUMP (sqrt(CAP)/2)
//#define NUMP 4157407LL
#define MAX_PS 11LL //because taking the product of the first 9 prime squares yields a result greater than 5*10^15

unsigned long long int squarefree(unsigned long long int n, unsigned long long int div_cap);
void enumerate_psquares (unsigned long long int cap,unsigned long long int pnum, unsigned long long int prod,unsigned long long int dprod);
unsigned long long int gcd_k_kprime(unsigned long long int k);


unsigned long long int p_divs[MAX_PS];
unsigned long long int num_divs;
unsigned long long int sum;
unsigned long long int * primes;
unsigned long long int * prime_squares;
unsigned long long int curr_cap;
char * p_div_mask;

unsigned long long int squarefree(unsigned long long int n, unsigned long long int div_cap)
{
  unsigned long long int dec = 0;
  unsigned long long int i = 0;
  unsigned long long int j = 0;
  unsigned long long int real_cap = (n < div_cap ) ? n + 1 : div_cap;
//  if (n == div_cap && n >= 10) printf("n equal to div_cap for n = %llu\n",n);
  while (j < num_divs && p_divs[j] < prime_squares[i] && p_divs[j] < real_cap)
  {
    dec += squarefree(n/p_divs[j],p_divs[j]);
    j++;
  }
  
  while (i < NUMP && prime_squares[i] < real_cap && prime_squares[i])  {
    while (j < num_divs && p_divs[j] < prime_squares[i] )
    {
      dec += squarefree(n/p_divs[j],p_divs[j]);
      j++;
    }
    if(!p_div_mask[i]) dec += squarefree(n/prime_squares[i],prime_squares[i]);
    i++;
  }
  
  while (j < num_divs && p_divs[j] < real_cap)
  {
   // printf("Prime divisors bigger than biggest square %llu %llu %llu\n",p_divs[j],real_cap,n);
    dec += squarefree(n/p_divs[j],p_divs[j]);
    j++;
  }

  if (dec >= n) printf("dec bigger than n");
  return n - dec;
}
unsigned long long int kprime(unsigned long long int k);

/*unsigned long long int kprime(unsigned long long int k)
{
  unsigned long long int j = 0;
  while (j < NUMP && primes[j] <= k)
  {
    if (!primes[j]) printf("%llu %llu\n",j,primes[j-1]);
    if (k == primes[j]) return 1;
    if (k % primes[j] == 0) return primes[j]*kprime(k/primes[j]) + k/primes[j];
    j++;
  }
}*/
unsigned long long int kprime(unsigned long long int k)
{
  if (k <= 1) return 0;
  unsigned long long int j;
  for (j = 2; j*j <= k; j++)
  {
    if (k % j == 0) return kprime(k/j)*j + (k/j)*kprime(j);
  }
  return 1;
}



void enumerate_psquares (unsigned long long int cap,unsigned long long int pnum, unsigned long long int prod,unsigned long long int dprod)
{
  sum += prod*squarefree(curr_cap/dprod,curr_cap/dprod+1);
//  printf("prod %llu, wieght %llu\n",prod,squarefree(TST_CAP/dprod,TST_CAP/dprod+1));;
  while(prime_squares[pnum] <= cap && prime_squares[pnum])
  {
    unsigned long long int curr_pow = 2;
    unsigned long long int accum = prime_squares[pnum];
    unsigned long long int curr_prime = primes[pnum];
    p_divs[num_divs] = primes[pnum];
    num_divs++;
    p_div_mask[pnum] = 1;
    while(accum <= cap)
    {
      if (accum == cap) printf("accum = cap %llu, %llu, %llu \n",cap,curr_prime,curr_pow);
      if (curr_pow % curr_prime == 0) enumerate_psquares(cap/accum,pnum+1,prod*accum,dprod*accum);
      else enumerate_psquares(cap/accum,pnum+1,prod*accum/curr_prime,dprod*accum);
      accum *= curr_prime;
      curr_pow++;
      
    }
    p_div_mask[pnum] = 0;
    pnum++;
    num_divs--;
    p_divs[num_divs] = 0;
  }
  return;
}
unsigned long long int gcd_k_kprime(unsigned long long int k)
{
  unsigned long long  int j;
  unsigned long long  int exp = 0;
  unsigned long long  int tmp;
  unsigned long long int prod = 1;
  for (j = 0; j < NUMP && primes[j] < k && primes[j]; j++)
  {
    exp = 0;
    tmp = prime_squares[j];
    if (k  % prime_squares[j] == 0)
    {
      exp += 2;
      k /= tmp;
      tmp = primes[j];
      prod *= tmp;
      while (k % tmp == 0)
      {
        k /= tmp;
        prod *= tmp;
        exp++;
      }
      
      if (exp % tmp == 0) prod *= tmp;
    }
  }
  
  return prod;
}

unsigned long long int gcd(unsigned long long int a, unsigned long long int b);

unsigned long long int gcd(unsigned long long int a, unsigned long long int b)
{
  if (b == 0) return a;
  else return gcd(b,a%b);
}

int main()
{
  char * mask = (char *)malloc(sqrt(CAP)/2);
  unsigned long long  int i;
  unsigned long long  int slow_sum = 0;  
  memset(p_divs, 0, sizeof(p_divs));  
  primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  prime_squares = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  p_div_mask = (char *)malloc(NUMP);
  if (!primes || ! prime_squares || !p_div_mask)
  {
    fprintf(stderr,"Out of memory.\n");
    exit(1);
  }
  memset(p_div_mask, 0, NUMP);  
  num_divs = 0;
  sum = 0;
  
  really_big_prime_mask_and_arr(mask,sqrt(CAP)/2, primes,NUMP);
  free(mask);
  
  for (i = 0; i < NUMP; i++) prime_squares[i] = primes[i]*primes[i];
  curr_cap = TST_CAP;

//  printf("%llu\n",prime_squares[NUMP-1]);
  enumerate_psquares(TST_CAP,0,1,1);
  unsigned long long int tmp_sum = 0;
  printf("The sum of gcd(k,k') for k <= %llu is %llu\n",(unsigned long long int)TST_CAP,sum-1);  
 /* for (i = 2; i <= TST_CAP; i++)
  {
    sum = 0;
    curr_cap = i;
    tmp_sum += gcd(i,kprime(i)); 
    enumerate_psquares(i,0,1,1);
    if (sum - 1 != tmp_sum)
    {
      printf("Algorithms don't match for n = %llu, exp %llu, gvn %llu\n",i,tmp_sum,sum-1);
    }
  }
  printf("%llu\n",tmp_sum); */
//  printf("%f\n",NUMP); 
}