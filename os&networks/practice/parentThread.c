#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <wait.h>

int n=5;
int a[5]={1,2,3,4,5};

void *count(void *args){
    printf("thread\n");
    for (int i=20;i<25;i++){
       printf("%d\n",i);
       sleep(1);
    }
}
int main(){
    pthread_t p;
    pthread_create(&p,NULL,count,NULL);
    printf("parent\n");

    for(int i=0;i<5;i++)
    {
        printf("%d\n",i);
        sleep(1);
    }
}