#include "stdio.h"
#include "stdlib.h"
#include "math.h"

int main()
{
  unsigned long long int cap = 100000000;
  unsigned long long int aprev = 1;
  unsigned long long int bprev = 2;
  unsigned long long int acurr = 0;
  unsigned long long int bcurr = 0;
  unsigned long long int c,p;
  unsigned long long int s = 0;
  while (1)
  {
    acurr = (bprev << 1) + aprev;
    bcurr = (acurr << 1) + bprev;
    aprev = acurr;
    bprev = bcurr;
    c = (-2 + sqrt(4 - 8*(1-acurr*acurr)))/4;
    p = acurr + 2*c + 1;
    if (p >= cap) break;    
    s += cap/p;
  }
  printf("sum: %llu\n",s);
}
