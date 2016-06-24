#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/* here, do your time-consuming job */

int main()
{
 
  long int c = 999999; //this program will find the sum of all primes less than 2(*c+1).
  unsigned long long int sum = 2;
  char mask[c];
  long int p = 0;
  memset (mask,1,c);
  long int i;
  for (i=0;i<c;i++)
  {
    if (mask[i] == 1)
    {
      long int inc = 1 + 2*(i+1);
      sum += inc;
      //printf("%ld\n",inc);
      long int j;
      for (j = i;j<c-inc;)
      {
        j += inc;
        mask[j] = 0;
      } 
    }
  }
  printf("prime sum %llu\n",sum);
}
