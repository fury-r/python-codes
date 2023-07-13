#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <wait.h>

int main(){
    pid_t a,b;
    int status;
    a=fork();
    b=fork();
    if(a==0){
        printf("child pid: %d",getpid());
        exit(0);
    }
    if(b==0){
        printf("child pid: %d",getpid());
        exit(1);
    }
    printf("First wait\n");
    a=wait(&status);
    printf("pid:%d status:%d\n",a,WEXITSTATUS(status));
    printf("Second wait\n");
    a=wait(&status);
    printf("pid:%d status:%d\n",a,WEXITSTATUS(status));
    return EXIT_SUCCESS;
}