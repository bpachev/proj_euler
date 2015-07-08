#include <stdio.h>
#include <stdlib.h>

int main()
{
  int i,j,k;
  int tmp;
  
  for (i = 1; i < 4; i++)  {
    for (j = 1; j < 10; j++) {
      if (j == i) continue;
      for (k = 1; k < 10; k++) {
        if (k == j || k == i) continue;
        tmp = i*100 + j*10 + k;
        printf("%d%d%d\n",tmp,tmp*2,temp*3);
      }
  }
  
}
