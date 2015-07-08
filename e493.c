#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#define URN_CAP 10
#define NUMB 20

int main()
{
  int d1,d2,d3,d4,d5,d6,d7;
  unsigned long long int sum = 0;
  unsigned long long int cval = 0;
  unsigned long long int cols[8];
  long int fact[URN_CAP+1];
  long int ncr[URN_CAP+1]; 
  memset(cols,0,sizeof(cols));
  fact[0] = 1;
  int i = 1;  
  for (i = 1; i <= URN_CAP; i++) fact[i] = i*fact[i-1];
  for (i = 0; i <= URN_CAP; i++) ncr[i] = fact[URN_CAP]/(fact[URN_CAP-i]*fact[i]);
  
  for (d1 = 0; d1 <= URN_CAP; d1++)
  {
    for (d2 = 0; d2 <= URN_CAP && d1+d2 <= NUMB; d2++)
    {
      for (d3 = 0; d3 <= URN_CAP && d1+d2+d3 <= NUMB; d3++)
      {
        for (d4 = 0; d4 <= URN_CAP && d1+d2+d3+d4 <= NUMB; d4++)
        { 
          for (d5 = 0; d5 <= URN_CAP && d1+d2+d3+d4+d5 <= NUMB; d5++)
          {
            for (d6 = 0; d6 <= URN_CAP && d1+d2+d3+d4+d5+d6 <=NUMB; d6++)
            {
              for (d7 = 0; d7 <= URN_CAP && d1+d2+d3+d4+d5+d6+d7 <= NUMB; d7++)
              {
                if(d1+d2+d3+d4+d5+d6+d7 == NUMB)
                {
                  //if(d1 > 1 && d6 > 4 &&d7&&d2&&d3&&d4&&d5) printf("%d red balls, %d blue balls, %d green balls, %d purple balls, %d orange balls, %d yellow balls, %d violet balls\n",d1,d2,d3,d4,d5,d6,d7);
                  int c1 = (d1 !=0) ? 1 : 0;
                  int c2 = (d2 !=0) ? 1 : 0;
                  int c3 = (d3!=0) ? 1 : 0;
                  int c4 = (d4!=0) ? 1 : 0;
                  int c5 = (d5!=0) ? 1 : 0;
                  int c6 = (d6!=0) ? 1 : 0;
                  int c7 = (d7!=0) ? 1 : 0;
                  unsigned long long int tmp = ncr[d1]*ncr[d2]*ncr[d3]*ncr[d4]*ncr[d5]*ncr[d6]*ncr[d7];
                  cols[c1+c2+c3+c4+c5+c6+c7] += tmp;
                  sum += tmp;
                }
                else continue;
              }

            }

          }

        }

      }

    }
  }
  for(i = 1; i<=7; i++)
  {
    printf("There are %llu ways to get %d distinct colors\n",cols[i],i);
    cval += cols[i]*i;
  }
  printf("There are %llu possible combinations, %llu exp\n",sum,cval);
}