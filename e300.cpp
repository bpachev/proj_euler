#include <vector>
#include <iostream>
#include <stdio.h>
#define n 4
#define G (2*n+1)
using namespace std;

vector<vector<int> > configs;
int grid[G][G];

void print_grid();
void enum_configs(int len_protein,int row,int col);
void add_config();


void enum_configs(int len_protein,int row,int col)
{
 //check for going outside of the grid or running into ourself
 if (row>=G || col >= G || row<0 || col < 0 || grid[row][col] || len_protein>=n) return;

 //mark the current cell as visited
 grid[row][col] = len_protein+1; 
 
 //if we've written out the entire protein
 if (len_protein==n-1)
 {
  add_config();
 }
 
 else
 {
  // keep extending the protein
  enum_configs(len_protein+1,row+1,col);
  enum_configs(len_protein+1,row,col+1);
  enum_configs(len_protein+1,row-1,col);
  enum_configs(len_protein+1,row,col-1);
 }
 //clear cell and backtrack
 grid[row][col] = 0;
 
}

void add_config()
{
 int i,j;
 vector<int> temp;
// print_grid();
 
 //find all connections
 for (i=0;i<G-1;i++)
 {
  for (j=0;j<G-1;j++)
  {
   if (grid[i][j])
   {
    if (grid[i][j+1])
    {
  //   cout << grid[i][j+1] << " " << grid[i][j] << endl; 
     temp.push_back((1<<(grid[i][j]-1))+(1<<(grid[i][j+1]-1)));
 //    cout << temp.back() << endl;    
    }
    if (grid[i+1][j])
    {
//     cout << grid[i+1][j] << " " << grid[i][j] << endl; 
     temp.push_back((1<<(grid[i][j]-1))+(1<<(grid[i+1][j]-1)));
 //    cout << temp.back() << endl;        
    }
   }
  }
 }
 if (temp.size() >= n)
 {
  configs.push_back(temp);
 }
 
  
}

void print_grid()
{
 int i,j;
 for (i=0;i<G;i++)
 {
  for (j=0;j<G;j++)
  {
   printf("%d ",grid[i][j]);
  }
  printf("\n");
 }
 cout << endl;
}

int main()
{
 int i,j,k;
 for (i=0;i<G;i++)
 {
  for (j=0;j<G;j++)
  {
   grid[i][j] = 0;
  }
 }
 
 //WLOG we can assume the first two elements point northward, or up.
 //And if we go to the left with the third element, a reflection maps it to something that went to the right on the third element.
 grid[n][n] = 1;
 grid[n-1][n] = 2;
 enum_configs(2,n-2,n);
 enum_configs(2,n-1,n+1);

 cout << configs.size() << endl;
 long long int sum = 0;
 for (i=1; i < 1<<n;i++)
 {
  int max = 0;
  for (j=0;j<configs.size();j++)
  {
  
   int nbonds = 0;
   for (k=0;k<configs[j].size();k++)
   {
    if (i==1&&j==0) cout << configs[j][k] << " " << (i&configs[j][k]) << endl; 
   
    if ((i&configs[j][k])==configs[j][k]) nbonds++;
   }
   cout << nbonds << endl;
   if (nbonds>max) max = nbonds;
  }
  cout << max << " " << i << endl;
  sum += max;
 }
 cout << "Sum: " << sum << endl;;
}
