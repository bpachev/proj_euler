//Benjamin Pachev May 2015


#include "primes.h"
#define CAP (5000000000000000LL)
//#define CAP 5000000LL
#define MASK_SIZE ((int)(sqrt(CAP)/2) + 1000)
//#define NUMP 500
#define MPDIVS 128
//#define NUMP (4157407LL)
#define NUMP (4157407LL)
//#define NUMP 4
typedef long long int LL;
LL * p_squares, *primes;
char * mask;
char * p_mask;
LL p_divs[MPDIVS];
LL num_ps;

LL arithmetic_derivative(LL n, LL p_num);
LL num_admissible(LL n, LL p_num);
LL slow_num_admissible(LL n);

void print_vec(LL * v, LL size)
{
  LL i;
  printf("[");
  for (i = 0; i < size; i++)
  {
    printf("%lld ",v[i]);
  }
  printf("]\n");
}

int main()
{
  LL i,j;
  mask = (char*)malloc(MASK_SIZE);
  primes = (LL *)malloc(NUMP*sizeof(LL));
  p_squares = (LL *)malloc(NUMP*sizeof(LL));
  p_mask = (char *)malloc(NUMP*sizeof(char));  
  if (!primes || !p_squares || !p_mask) printf("Memory Error\n");
  else printf("AH'M still ALIIVE!!!\n");
  really_big_prime_mask_and_arr(mask,MASK_SIZE,primes, NUMP);  
  
  //initialize primes 
  for (i = 0; i < NUMP; i++)
  {
    p_squares[i] = primes[i]*primes[i];
  }

  // I don't trust memset :)
  for (i = 0; i < MPDIVS; i++)
  {
    p_divs[MPDIVS] = 0;
  }

  //zero out p_mask
  for (i = 0; i < NUMP; i++)
  {
    p_mask[i] = 0;
  }
  num_ps = 0;
  printf("CUMPLETED initialization\n");
  printf("ad_sum(%lld) %lld\n",CAP,arithmetic_derivative(CAP,0) - 1);
 /* p_divs[0] = 3;
  p_divs[1] = 5;
  num_ps = 2;
  p_mask[1] = 1;
  p_mask[2] = 1;  
  printf("n_ad(17,0) %llu\n",num_admissible(17,0));*/
}

LL num_admissible(LL n, LL p_num)
{
  //printf("Called with n = %llu, p_num = %llu\n",n,p_num);
  if (!n) return 0;
  if (n == 1)
   {
    // printf("returned 1\n");
     return 1;
   }
  LL sum = n;
  LL i;
  
  for (i = p_num; i < num_ps; i++)
  {
    if (p_divs[i] > n) continue;
    sum -= num_admissible(n/p_divs[i],i+1);
  }
  
  i = p_num - num_ps; //If we are past the excluded primes, then we've started on the squarefree part.
  if (i < 0) i = 0; // still working through the list of excluded primes;
  
  for (;i < NUMP; i++)
  {
    if (p_squares[i] > n) {
      //printf("RETURNEDb n:%lld, sq:%lld sum: %llu\n",n,p_squares[i],sum);
      return sum;
    }
    if (!p_mask[i]) {
     // printf("sum: %llu\n",sum);
      sum -= num_admissible(n/p_squares[i],i + num_ps + 1);
    }
  }
 // printf("RETURNED %llu\n",sum);
  return sum;
}

LL slow_num_admissible(LL n)
{
  LL i,j,is_good;
  LL s = 0;
  for (i = 1; i <= n; i++)
  {
    is_good = 1;
    for (j = 0; j < num_ps; j++)
    {      
      if (i % p_divs[j] == 0)  is_good = 0;  
    }
    
    for (j = 0; p_squares[j] <= n; j++)
    {
      if (i % p_squares[j] == 0)
      {
        is_good = 0;
        break;
      }
    }
    
    if (is_good) s++;
  }
  return s; 
}

LL arithmetic_derivative(LL n, LL p_num)
{
  //printf("Called with n = %llu, p_num = %llu, num_ps = %llu pdivs[0] = %llu\n",n,p_num,num_ps,p_divs[0]);
  LL pow = 1;
  LL sum = 0;
  if (p_num >= NUMP) {
   // printf("Only %d primes\n",NUMP);
  //  printf("Returned %llu\n",num_admissible(n,0));
  /*  LL f = num_admissible(n,0);
    LL sl = slow_num_admissible(n); 
    if (f != sl)
    {
      printf("Discrepancy for n = %lld\n",n);
    }*/
    return num_admissible(n,0);
  }
  LL p = primes[p_num];
  LL accum = p;
  if (!n) return 0;
  if (n == 1) return 1;
  if (p_squares[p_num] > n) {
    // printf("Returned %llu\n",num_admissible(n,0));
    //LL f = num_admissible(n,0);
    //LL sl = slow_num_admissible(n); 
    /*if (f != sl)
    {
      printf("Discrepancy for n = %lld, npdivs: %lld, f:%lld, s:%lld\npdivs: ",n,num_ps,f,sl);
      print_vec(p_divs,num_ps);
      
    } */   
     return  num_admissible(n,0);
   }

  
  while (accum <= n) {
    if (pow == p) {
      //everything divisible by p^p OR a higher power of p
      sum += accum*arithmetic_derivative(n/accum,p_num);
      return sum;
    }

    //everything divisible by EXACTLY p^pow
    else if (pow > 1) {
      // add p to the blacklist
      p_mask[p_num] = 1;
      p_divs[num_ps] = p;
      num_ps++;
      sum += (accum/p)*arithmetic_derivative(n/accum,p_num + 1);
      num_ps--;
      p_divs[num_ps] = 0;
      p_mask[p_num] = 0;
    }

    //everything not divisible by p^2.
    else {
      sum += arithmetic_derivative(n,p_num + 1);
    }

    pow++;
    if (accum > n/p) break;
    accum *= p;
  }
  return sum;
}


