#include "primes.h"

#define CAP 100000000000
#define TOT 16*12*10*6*4*2 //TOT(510510) = TOT(2*3*5*7*11*13*17)

unsigned long long int R[MAX_CACHE];
//unsigned long long int fast_tot_sum_mod(unsigned long long int n,unsigned long long int mod);

unsigned long long int fast_tot_sum(unsigned long long int n);
long long int fast_tot_sum_mod(unsigned long long int n,unsigned long long int mod);
unsigned long long int F(unsigned long long int n);


int main()
{
  long long int i,j;
  unsigned long long int sum = 0;
  unsigned long long int coeff = 1;
  unsigned long long int mod = 1000000000;
  unsigned long long int n = CAP;
  unsigned long long int div2,div3,div5,div7,div11,div13,div17;
  char * mask = (char*)malloc(MAX_CACHE);


  memset(mask,1,MAX_CACHE);
  R[0] = 0;
  R[1] = 0;
  for (i = 2; i < MAX_CACHE; i++)  {
    R[i] = i;
  }

  //precompute values of sum_{i=1}^{i=n}tot(i)
  for (i = 2; i < MAX_CACHE; i++) {
    //if prime
    if (mask[i]) {
      R[i] = i - 1;
      for (j = i; j < MAX_CACHE; j += i) {
        R[j] = R[j] - (R[j] / i);
        mask[j] = 0;
      }
    }
    //to compute the sum
    R[i] = (R[i] + R[i-1]) % mod;
  }

 /* while (n)
  {
    printf("Coeff: %llu, tot_sum: %llu, n %llu\n",coeff,fast_tot_sum_mod(n,mod), n);
    sum = (sum + coeff * (fast_tot_sum_mod(n,mod) + 1)) % mod;
    n = n / 2;
    i++;
    coeff = ((5 + i) * coeff) / i;
    //coeff should equal 5 + i choose 5.
  }*/
//  memset(R,0,sizeof(R));
 //n = CAP;
  for (div2 = 1; div2 <= CAP; div2 *= 2) {
    for (div3 = div2; div3 <= CAP; div3 *= 3) {
      for (div5 = div3; div5 <= CAP; div5 *= 5) {
        for (div7 = div5; div7 <= CAP; div7 *= 7) {
          for (div11 = div7; div11 <= CAP; div11 *= 11) {
            for (div13 = div11; div13 <= CAP; div13 *= 13) {
               for (div17 = div13; div17 <= CAP; div17 *= 17) {
                 sum += (fast_tot_sum_mod(n/div17,mod) + 1) % mod;
  } } } } } } }
  


  sum = (sum * TOT) % mod;
  printf("Sum: %llu\n",sum);
}

//for algorithmic reasons, (i.e recurison) returns one less than the actual sum.
unsigned long long int fast_tot_sum(unsigned long long int n)
{
  if (n == 1) return 0;
  if (n < MAX_CACHE) {
    if (R[n]) return R[n];
  }

  unsigned long long int s = F(n);
  unsigned long long int k = n/2;
  unsigned long long int m = 2;
  unsigned long long int j;
  
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    s -= (j+1) * fast_tot_sum(k);
    m += j + 1;
  }
  if (n < MAX_CACHE) R[n] = s;
  return s;
}
//for algorithmic reasons, (i.e recurison) returns one less than the actual sum.
long long int fast_tot_sum_mod(unsigned long long int n, unsigned long long int mod)
{
  if (n == 1 || !n) return 0;
  if (n < MAX_CACHE) {
    if (R[n]) return R[n];
  }
  long long int s = ((n % mod)*((n-1) % mod) / 2) % mod;
  long long int k = n/2;
  long long int m = 2;
  long long int j;
  
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    long long int temp = ((j+1) * fast_tot_sum_mod(k,mod)) % mod;
    if (temp > s) {
      s = s - temp + mod;
    }

    else {
      s = ( s - temp ) % mod;
    }
    m += j + 1;
  }
  if (n < MAX_CACHE) R[n] = s % mod;
  return s % mod;
}

//Auxiallary function
unsigned long long int F(unsigned long long int n)
{
  return n * (n - 1)/2;
}


