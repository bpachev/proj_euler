#include "stdio.h"
#include "stdlib.h"
#include "math.h"

#define CAP 100000000

int main()
{
  long long x = 0;
  long long y = 0;
  unsigned long long sum = 0;
  for (x = 3; x <= (CAP+4)/4; x++)
  {
    long long inc = (x*x > CAP) ? (x - ceil(sqrt(x*x-CAP))) / 2 : (x - 1)/2; 
    sum += inc;
    //printf("x %llu inc %llu\n",x,inc); 
//    for (y = x - 2; y > 0 && (x+y)*(x-y) <= CAP; y -= 2)
  //  {
 //     printf("x = %llu, y = %llu k = %llu\n",x,y,(x+y)*(x-y));
      //sum++;
    //}
  }
  printf("%llu\n",sum); 
}
