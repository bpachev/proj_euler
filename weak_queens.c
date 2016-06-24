#include "proj_euler.h"
#define n 14

int tqs[n]; // flipped version of qs

//backtracking solution to chessboard problem
LL backtrack(int* qs, int curr_row,int rows,int cols,int weakness)
{
 LL s = 0;
 int i,j;
 if (curr_row >= rows) return 1;

 for (i=0; i < cols; i++)
 {
   int flag = 1;

   for (j=((curr_row-weakness)>0) ? (curr_row-weakness) : 0; j < curr_row; j++)
	 {
		 if (i==qs[j] || curr_row-j==i-qs[j] || curr_row-j == qs[j]-i)
		 {
			 flag=0;
			 break;
		 }
	 }

	 if (flag)
	 {
		qs[curr_row] = i;
		s += backtrack(qs,curr_row+1,rows,cols,weakness);
	 }
 }
 return s;
}

void flip_qs(int *src,int *dst,int nqs,int ncols)
{
 int i;
 for (i=0;i<nqs;i++)
 {
  dst[i] = ncols-src[nqs-i-1]-1;
 }
}

//computes all of the Q(n,w) w >= 2 (at once)
//Basically, at iteration i, we've computed a valid positioning of i queens
//We start a regular backtrack going both up and down
//This requires flipping the qs array for the up direction
LL big_backtrack(int* qs, int curr_row,int rows,int cols,int min_weakness)
{
 LL s = 0;
 int i,j;
 if (curr_row >= rows) return 1;

 for (i=0; i < cols; i++)
 {
   int flag = 1;

   for (j=0; j < curr_row; j++)
	 {
		 if (i==qs[j] || curr_row-j==i-qs[j] || curr_row-j == qs[j]-i)
		 {
			 flag=0;
			 break;
		 }
	 }

	 if (flag)
	 {
			qs[curr_row] = i;

		if (curr_row>=min_weakness && curr_row <rows-1)
		{
			int rows_rem = rows-curr_row-1;
//			printf("rows_rem %d\n",rows_rem);
			LL tmp1 = backtrack(qs,curr_row+1,rows-rows_rem/2,cols,curr_row);
			flip_qs(qs,tqs,curr_row+1,cols);
			s += tmp1*backtrack(tqs,curr_row+1,curr_row+1+rows_rem/2,cols,curr_row);
		}
		s += big_backtrack(qs,curr_row+1,rows,cols,min_weakness);
	 }
 }
 return s;

}

int main()
{
	int board[n][n];
	int qs[n];
	printf("Sols for %d x %d board %llu\n",n,n,big_backtrack(qs,0,n,n,4));
}