#include <stdio.h>
#include <wait.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
    pid_t a,b;
    int status=0;
    a=fork();
    b=fork();
    if(a==0){
        printf("Child PID: %d\n",getpid());
        _exit(EXIT_SUCCESS);
    }
    else if(b==0)
    {
        printf("Child PID: %d\n",getpid());
        _exit(EXIT_FAILURE);
    }
    printf("First wait\n");
    a=wait(&status);
    printf(" PID:%d status:%d\n",a,WEXITSTATUS(status));
    printf("Second wait\n");
    a=wait(&status);
    printf("PID:%d status:%d\n",a,WEXITSTATUS(status));
    return EXIT_SUCCESS;
    
}