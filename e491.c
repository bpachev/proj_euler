#include <stdlib.h>
#include <stdio.h>

int main()
{
  int d0,d1,d2,d3,d4,d5,d6,d7,d8,d9;
  d0 = 0;
  d1 = 0;
  d2 = 0;
  d3 = 0;
  d4 = 0;
  d5 = 0;
  d6 = 0;
  d7 = 0;
  d8 = 0;
  d9 = 0;
  unsigned long long int sum = 0;
  unsigned long long int fact = 362880;
  int divs[3];
  divs[0] = 2;
  divs[1] = 1;
  divs[2] = 2;
  
  for (d0 = 0; d0 <= 2; d0++) {
    for (d1 = 0; d1 <= 2; d1++) {
      for (d2 = 0; d2 <= 2; d2++) {
        for (d3 = 0; d3 <= 2; d3++) {
          for (d4 = 0; d4 <= 2; d4++) {
            if (d4 + d3 + d2 + d1 + d0 == 10)
            {
              if ((2*(5+6+7+8+9) - 2*(1+2+3+4)) % 11 == 0)
              {
                printf("4 %d\n",divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]);
                sum += (10-d0)*fact*(8+d0)*fact/(divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]);
                break;
              }
            }
            for (d5 = 0; d5 <= 2; d5++) {
              if (d5 + d4 + d3 + d2 + d1 + d0 == 10 && (2*(6+7+8+9) + 2 *(1 - d1) + 4*(1-d2) + 6*(1-d3) + 8*(1-d4) + 10*(1 - d5)) % 11 == 0)
              {
                printf("5 %d\n", d5);
                sum += (10-d0)*fact*(8+d0)*fact/(divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]*divs[d5]*16);
                break;
              }
              for (d6 = 0; d6 <= 2; d6++) {
                if (d6 + d5 + d4 + d3 + d2 + d1 + d0 == 10 && (2*(7+8+9) + 2 *(1 - d1) + 4*(1-d2) + 6*(1-d3) + 8*(1-d4) + 10*(1 - d5) + 12*(1-d6)) % 11 == 0)
                {
                  printf("6 %d %d %d %d %d %d %d inc %llu\n",d0,d1,d2,d3,d4,d5,d6,(10-d0)*fact*(8+d0)*fact/(divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]*divs[d5]*divs[d6]*8));
                  sum += (10-d0)*fact*(8+d0)*fact/(divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]*divs[d5]*divs[d6]*8);
                  break;
                }

                for (d7 = 0; d7 <= 2; d7++) {
                  if (d7 + d6 + d5 + d4 + d3 + d2 + d1 + d0 == 10 && (2*(8+9) + 2 *(1 - d1) + 4*(1-d2) + 6*(1-d3) + 8*(1-d4) + 10*(1 - d5) + 12*(1-d6) + 14*(1-d7)) % 11 == 0)
                  {
                   // printf("7 %d\n",divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]*divs[d5]*divs[d6]*divs[d7]);
                    sum += (10-d0)*fact*(8+d0)*fact/(divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]*divs[d5]*divs[d6]*divs[d7]*4);
                    break;
                  }

                  for (d8 = 0; d8 <= 2; d8++) {
                    d9 = d8 + d7 + d6 + d5 + d4 + d3 + d2 + d1 + d0 - 10;
                    if (d9 < 3 && d9 >= 0  && (18*(1-d9) + 2 *(1 - d1) + 4*(1-d2) + 6*(1-d3) + 8*(1-d4) + 10*(1 - d5) + 12*(1-d6) + 14*(1-d7) + 16*(1-d8)) % 11 == 0)
                    {
                     // printf("9 %d %d%d%d%d%d%d%d%d%d%d\n",d9,divs[d0],divs[d1],divs[d2],divs[d3],divs[d4],divs[d5],divs[d6],divs[d7],divs[d8],divs[d9]);
                      sum += (10-d0)*fact*(8+d0)*fact/(divs[d0]*divs[d1]*divs[d2]*divs[d3]*divs[d4]*divs[d5]*divs[d6]*divs[d7]*divs[d8]*divs[d9]);
                    }

                  }
                }
              }
            }
          }
        }
      }
    }
  }
  printf("There are %llu double 0-9 pandigital numbers divisible by 11\n",sum);  
}
