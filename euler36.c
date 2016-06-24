#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_DIGITS 6
#define SIX_DIGIT(d1,d2,d3,d4,d5,d6) (d1*100000+d2*10000+d3*1000+d4*100+d5*10+d6)
#define FIVE_DIGIT(d1,d2,d3,d4,d5) (d1*10000+d2*1000+d3*100+d4*10+d5)
#define FOUR_DIGIT(d1,d2,d3,d4) (d1*1000 + d2*100 + d3*10 + d4)


int is_bpalindrome(int n);

int main()
{
  int sum = 0;
  int i,j,k,l;
  int temp;

  
  for (i = 0 ; i < 9; i++)
  {
    for (j = 0; j < 10; j++)
    {
      for (k = 0; k< 10; k++)
      {
        
        if (i>0)
        {
          temp = SIX_DIGIT(i,j,k,k,j,i);
          if (is_bpalindrome(temp)) {sum += temp; printf("%d is a base 2 palindrome.\n",temp);}
        }
        
        else if (j > 0)
        {
          temp = FOUR_DIGIT(j,k,k,j);
          if (is_bpalindrome(temp)) {sum += temp; printf("%d is a base 2 palindrome.\n",temp);}
          temp = FIVE_DIGIT(j,k,0,k,j);
          for (l = 0; l < 10; l++)
          {
            if (is_bpalindrome(temp)) {sum += temp; printf("%d is a base 2 palindrome.\n",temp);}
            temp += 100;
          }
        }
        
        else if (i==0 && j == 0)
        {  
          if (is_bpalindrome(k)) {sum += k; printf("%d is a base 2 palindrome.\n",k);}
          if (is_bpalindrome(k*11)) {sum += k*11;printf("%d is a base 2 palindrome.\n",k*11);}
          for (l = 0; l < 10; l++)
          {
            temp = k*101+l*10;
            if (is_bpalindrome(temp)) {sum += temp; printf("%d is a base 2 palindrome.\n",temp);}
          }
        }

      }
    }
  }
  
  printf("Sum: %d\n9119: %d\n",sum,is_bpalindrome(9119));
  
}

int is_bpalindrome(int n)
{
  int num_bits = (int)log2(n) + 1;
  int i,bh,bl;
  if (!(n&1)) return 0;
  for (i = 0; i < num_bits/2; i++)
  {
    bh = (1 << i) & n;
    bl = (1 << (num_bits-i-1)) & n;
    if (n == 121) printf("The %dth digit of %d is %d, comp %d\n",i+1,n,1<<i,1 << (num_bits-i));
    if ((bh && !bl) || (bl && !bh)) return 0;
  }  
  return 1;  
}