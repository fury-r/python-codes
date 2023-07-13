#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

void *count(void *args);


int main(){
    pthread_t a;
    int i;
    pthread_create(&a,NULL,count,NULL);
    printf("process\n");
    for ( i=25;i<32;i++){
        printf("%d\n",i);
        sleep(1);
    }
}
void *count(void *args){
    printf("Thread \n");
    int j;
    for ( j=0;j<5;j++){
        printf("%d\n",j);
        sleep(1);
    }
}