#include "proj_euler.h"

#define CAP 1000000000000LL
#define PCAP 100000000LL
#define NUMP 5761455LL

/*#define CAP 100
#define PCAP 21
#define NUMP*/ 
//typedef long long int LL;
//typedef unsigned long long int ULL;


LL * primes;
LL * psums;

LL s;
LL mod;

LL f(LL n)
{
  if (n % 2==0) return (((n/2)%mod) * ((n+1) % mod)) % mod; 
  else return ((n%mod) * (((n+1)/2)%mod))%mod;
}

LL prods(LL prod, LL startNum,LL sign,LL NP)
{
  if (prod > CAP) return;
  
  LL i;
  
  for (i = startNum;i < NP;i++)
  {
    if (primes[i] > CAP / prod) return;
    LL m = prod * primes[i];
    if (sign)
    {
      s = (s - ((m%mod)*f(CAP/m) % mod) + (primes[i] * (CAP/m)) % mod) % mod;
      if (s < 0) s += mod;
      prods(m,i+1,0,NP);
    }
    
    else
    {
      s = (s + ((m%mod)*f(CAP/m) % mod) - (primes[i] * (CAP/m)) % mod) % mod;    
      if (s < 0) s += mod;
      prods(m,i+1,1,NP);
    }
  } 
}

LL pi(LL n,LL realNumPrimes)
{
  LL pos = big_bin_search(primes,0,realNumPrimes-1,n);
  return pos;
}

int main()
{
  printf("Hello world\n");
  fprintf(stderr,"Hello world\n");
  
  primes = (LL *)malloc(NUMP*sizeof(LL)); 
  psums = (LL *)malloc(NUMP*sizeof(LL));
  char * mask = (char*)malloc(PCAP);
  memset(mask,1,PCAP);
  memset(primes,0,NUMP*sizeof(LL));
  memset(psums,0,NUMP*sizeof(LL));
  LL i,j,k;
  mod = 1000000000LL;
  k = 0;

  printf("started sieving\n");  
  for (i=2;i<PCAP;i++)
  {
    if (mask[i])
    {
      primes[k] = i;
      if (!k) psums[k] = i;
      else psums[k] = (psums[k-1] + i) % mod;
      k++;
      for (j = i+i;j<PCAP;j+=i)
      {
        mask[j] = 0;
      }
    }
  }
  free(mask);
  printf("%lld nump\n",k);    
  fprintf(stderr,"%lld nump\n",k);  
  s = f(CAP);
  
  LL d = pi(CAP/PCAP,k);
  prods(1,0,1,d);
  printf("S after prod %lld\n",s);
  fprintf(stderr,"S after prod %lld\n",s);
  
  for (i = d; i < k; i++)
  {
    if (primes[i] > CAP/primes[i]) break;
    LL hi = pi(CAP/primes[i],k);
//    printf("%lld %lld\n",hi,primes[i]);
    LL psum = psums[hi-1] - psums[i-1];
    s = (s - primes[i]*(psum + i-hi) % mod) % mod;
    if (s < 0) s += mod;
  }
  
  printf("Sum: %lld \n",s-1);
  fprintf(stderr,"Sum: %lld \n",s-1);  
} 
