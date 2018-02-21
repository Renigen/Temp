#include <stdio.h>
#include <stdlib.h>

int main()//splice later
{
  pid_t  pid;
  /* fork another process */
  pid = fork();
  if (pid < 0) { /* error occurred */
    fprintf(stderr, "Fork Failed");
    exit(-1);
  }
  else if (pid == 0) { /* child process */
    execvp(args[0], args);
  }
  else { /* parent process */
    /* parent will wait for the child to complete */
    wait (NULL);
    printf ("\nChild Complete\n");
    exit(0);
  }
}
