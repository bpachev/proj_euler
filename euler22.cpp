#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <sys/stat.h>
#include <sys/mman.h> 
#include <errno.h>
#include <string.h>
#include <stdarg.h>
#include <fcntl.h>
#include <ctype.h>

using namespace std;
enum {READ=0,DELIM=1};

typedef struct
{
  char * name;
  int size;
} NAME;

NAME* names;

void die(const char* msg,...);
int cmp_names(const void* name1, const void* name2);
int lexo_score(NAME n);

int lexo_score(NAME n)
{
  int s = 0;
  int k;
  for (k=0;k<n.size;k++)
  {
    s += n.name[k] - 'A' + 1;
  }
  return s;
}


int cmp_names(const void* name1,const void* name2)
{
  NAME * n1 = (NAME *)name1;
  NAME * n2 = (NAME *)name2;
  int len = (n1->size < n2->size) ? n1->size : n2->size;  
  int i;
  
  for (i=0; i < len; i++)
  {
    if (n1->name[i] < n2->name[i]) return -1;
    if (n1->name[i] > n2->name[i]) return 1;
  }
  
  if (n1->size > n2->size) return 1;
  if (n1->size < n2->size) return -1;
  else return 0;
}


int main()
{
  char *f;
  struct stat s;
  size_t size = 1;
  const char * filename = "p022_names.txt";
  int fd;
  int status;
  int i;
  int state = DELIM;
  char* temp_name;
  int begin = 0;
  int num_names = 0;
  char *c;
  fd = open(filename, O_RDONLY);
  if (fd < 0) die("open %s failed: %s", filename, strerror (errno));
//  printf("Hello world\n");  
  
  status = fstat(fd, &s);
//  printf("Hello world\n");  
  
  size = s.st_size;
//  printf("fsize = %lu\n",size);
  names = (NAME*)malloc(sizeof(NAME)*size/6); 
  
  c = (char *)mmap(0, size, PROT_READ, MAP_PRIVATE, fd, 0);
  if (c == MAP_FAILED) die("Error mapping memory:%s",strerror(errno));
  
  for (i = 0; i < size; i++)
  {

    if (c[i] == '\"')
    {
      if (state == DELIM)
      {
        begin = i;
        temp_name = &c[i]+1;
      } 
      
      if (state == READ)
      {
        if (num_names >= size/6)
        {
          printf("Not enough names\n");
          break;
        }
        names[num_names].name = temp_name;
        names[num_names].size = i - begin - 1;
        num_names++;
      }
//      printf("%d\n",i);
        state = state ^ 1;
    } 
  }
  
  qsort(names, num_names, sizeof(NAME),cmp_names);
  int j;
  unsigned long long int score = 0;
  for (j=0;j<num_names;j++) 
  {
    score += (j+1)*lexo_score(names[j]);
  }
//  printf("foo\n");  
 
  printf("total score: %llu, num_names %d\nlname %.*s\n",score,num_names,names[num_names-1].size,names[num_names-1].name);
}


void die(const char* msg, ...)
{
  va_list ap;
  va_start(ap,msg);
  
  fprintf(stderr, "fatal_error: ");
  vfprintf(stderr, msg, ap);
  va_end(ap);
  fputc('\n',stderr);
  exit(1);
}
