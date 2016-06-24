#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <ctype.h>
#define ROWS 100
#define FILENAME "p067_triangle.txt"

int triangle[ROWS][ROWS];
unsigned long int paths[ROWS][ROWS];

unsigned long int max_sum(int row,int col);

int main()
{
  FILE* f = fopen(FILENAME,"r");
  memset(triangle,0,sizeof(triangle));
  memset(paths,0,sizeof(paths));
  char c;
  int col = 0;
  int row = 0;
  int d = 0;
  while ((c=fgetc(f)) != EOF)
  {
     if (c==' ') 
     {
       triangle[row][col] = d;
       d = 0;
       col++;
       continue;
     }

     if (c=='\n') 
     {
       triangle[row][col] = d;
       row++;
       col = 0;
       d = 0;
       continue;
     }

     d = 10*d + c - '0';     
  }
  if (d) triangle[row][col]=d; 

  /*for (int i=0;i<ROWS;i++)
  {
    for (int j=0;j<ROWS;j++)
    {
      printf("%d ",triangle[i][j]);
    }
    printf("\n");
  }*/

  printf("Max path sum: %lu\n",max_sum(0,0));
}

unsigned long int max_sum(int row,int col)
{
//  if(row==0) printf("\nrow %d col %d\n,%d",row,col,triangle[row][col]);
  if (row==ROWS-1) return triangle[row][col]; //base case, bottom of triangle
  if (paths[row][col]) return paths[row][col]; //dynamic programming aspect, avoids caculating things it has already calculating.
  int t = triangle[row][col]; //don't access twice
  unsigned long int a = t + max_sum(row+1,col);
  unsigned long int b = t + max_sum(row+1,col+1);
  unsigned long int temp = (a>b) ? a : b;
  paths[row][col] = temp;
  return temp;
}

