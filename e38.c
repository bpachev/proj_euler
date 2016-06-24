#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ispdigital(int* num);

int ispdigital(int* num)
{
  int i;  
  int m[10];
  memset(m,0,sizeof(m));
  
  for (i = 0; i < 10;i++)
  {
    if (m[num[i]]) return 0;
    m[num[i]] = 1;
  }
  return 1;
}



int main()
{
  int i,j,k,l;
  int tmp;
  int* tmp_digits = (int*)malloc(9*sizeof(int));
  
  for (i = 1; i < 9; i++)  {
    for (j = 1; j < 9; j++) {
      if (j == i) continue;
      for (k = 1; k < 9; k++) {
        if (k == j || k == i) continue;
        tmp = 9000 + 100*i + 10*j + k;
        tmp_digits[0] = 9;
        tmp_digits[1] = i;
        tmp_digits[2] = j;
        tmp_digits[3] = k;
        tmp_digits[4] = ((2*tmp))/10000;
        tmp_digits[5] = ((2*tmp)%10000)/1000;
        tmp_digits[6] = ((2*tmp)%1000)/100;
        tmp_digits[7] = ((2*tmp)%100)/10;
        tmp_digits[8] = (2*tmp)%10;
        if(ispdigital(tmp_digits)) printf("%d%d\n",tmp,2*tmp);        
      }
    }
  }
}

