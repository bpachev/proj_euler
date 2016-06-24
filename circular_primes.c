#include "primes.h"
#define CAP 1000000

int is_circular(int p, char* mask);

int is_circular(int p, char* mask)
{
  int a,b,c,d,e,f;
  if (p > 100000)
  {
    GET_SIX_DIGITS(a,b,c,d,e,f,p)
    if (!MASK_WITH_CHECK(SIX_DIGIT(f,a,b,c,d,e),mask) || !MASK_WITH_CHECK(SIX_DIGIT(e,f,a,b,c,d),mask) || !MASK_WITH_CHECK(SIX_DIGIT(d,e,f,a,b,c),mask) ||
      !MASK_WITH_CHECK(SIX_DIGIT(c,d,e,f,a,b),mask) || !MASK_WITH_CHECK(SIX_DIGIT(b,c,d,e,f,a),mask)) return 0;
    return 1;
  }  
  else if (p > 10000)
  {
    GET_FIVE_DIGITS(a,b,c,d,e,p)
    if (!MASK_WITH_CHECK(FIVE_DIGIT(e,a,b,c,d),mask) || !MASK_WITH_CHECK(FIVE_DIGIT(d,e,a,b,c),mask) 
      || !MASK_WITH_CHECK(FIVE_DIGIT(c,d,e,a,b),mask) || !MASK_WITH_CHECK(FIVE_DIGIT(b,c,d,e,a),mask)) return 0;
    return 1;
  }
  else if (p > 1000)
  {
    GET_FOUR_DIGITS(a,b,c,d,p)
    if (!MASK_WITH_CHECK(FOUR_DIGIT(d,a,b,c),mask) || 
      !MASK_WITH_CHECK(FOUR_DIGIT(c,d,a,b),mask) || !MASK_WITH_CHECK(FOUR_DIGIT(b,c,d,a),mask) ) return 0;
    return 1;
  }
  else if (p > 100)
  {
    a = p/100;
    b = (p%100)/10;
    c = p % 10;
    if (!MASK_WITH_CHECK(b*100+c*10+a,mask) || !MASK_WITH_CHECK(c*100 + a*10 + b,mask)) return 0;
    else return 1;
  }  
  else if (p > 10)
  {
    a = p/10;
    b = p % 10;
//    printf("%d : %d\n",b*10+a,MASK_WITH_CHECK(b*10+a,mask));
    if (!MASK_WITH_CHECK(b*10+a,mask)) return 0;
    return 1;
  }
  else return 1;
}

int main()
{
  char * mask = (char *)malloc(CAP/2);
  int * primes = (int *)malloc(P_UNDER_MILLION*sizeof(int));
  prime_mask_and_arr(mask, CAP/2, primes, P_UNDER_MILLION);
  int i;
  int num_circular_primes = 0;
  
  for (i = 0; i < P_UNDER_MILLION; i++)
  {
    if (is_circular(primes[i], mask)) 
    { 
      num_circular_primes++;
    }
  }
  
  printf("There are %d circular primes under one million.\n",num_circular_primes); 
}