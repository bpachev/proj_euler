#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "string.h"

#define CAP 1000000
#define THRESH 10

int main()
{
  int i;
  long long x = 0;
  long long y = 0;
  unsigned long long sum = 0;
  int mask[CAP+1];
  for (i = 0; i <= CAP; i++) mask[i] = 0;
  for (x = 3; x <= (CAP+4)/4; x++)
  {
   // long long inc = (x*x > CAP) ? (x - ceil(sqrt(x*x-CAP))) / 2 : (x - 1)/2; 
 //   sum += inc;
    //printf("x %llu inc %llu\n",x,inc); 
    for (y = x - 2; y > 0 && (x+y)*(x-y) <= CAP; y -= 2)
    {
    //  printf("x = %llu, y = %llu k = %llu\n",x,y,(x+y)*(x-y));
      mask[(x+y)*(x-y)]++;
    }
  }

  for (i = 4; i <= CAP; i+=4)
  {
    if (mask[i] && mask[i] <= THRESH) sum++;
  } 

  printf("%llu\n",sum);
}
