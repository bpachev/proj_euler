#include "stdio.h"
#include "stdlib.h"
#define CAP 100000

int main()
{
  unsigned long long int cap = 1000000000000;
  unsigned long long int aprev = 1;
  unsigned long long int bprev = 2;
  unsigned long long int acurr = 0;
  unsigned long long int bcurr = 0;
  int i;
  for (i = 0; i < CAP; i++)
  {
    while (1)
    {
      acurr = (bprev << 1) + aprev;
      bcurr = (acurr << 1) + bprev;
      aprev = acurr;
      bprev = bcurr;
      if (acurr > cap) break;
    }
    printf("There are %llu blue chips.\n",(acurr + 1) >> 1);
  }
}
