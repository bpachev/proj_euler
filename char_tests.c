#include <stdio.h>

int main()
{
  char * c = "c:g36j<<";
  int i = 0;
  
  while (*c)
  {
    printf("%c",(*c)-i);
    c++;
    i++;
  }
  printf("\n");
}