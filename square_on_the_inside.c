#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int num_square_quads(int m);
int gcd(int a, int b);

int main()
{
  printf("Number of quadrilaterals containing a square number of lattice points %d\n",num_square_quads(100));
}

int gcd(int a, int b)
{
  if (b == 0) return a;
  else return gcd(b,a%b);
}


int num_square_quads(int m)
{
  int i,a,b,c,d;
  int gcds[m][m];
  int is_square[4*m*m];
  memset(gcds,0,sizeof(gcds));
  memset(is_square,0,sizeof(is_square));
  int s = 0;

  for (i = 1; i <= 2*m; i++)
  {
    is_square[i*i] = 1;
  }

  for (a = 1; a <= m; a++)  {
    for (b = 1; b <=m; b++)  {
      for (c = 1; c <= m; c++) {
        for (d = 1; d <= m; d++) {
          int points = (a*b + b*c + c*d + d*a - gcd(a,b) - gcd(b,c) - gcd(c,d) - gcd(d,a)+2)/2;
          s += is_square[points];
        }
      }
    }
  }
  return s;
}
