#include <stdio.h>
#include <unistd.h>
#include <wait.h>
#include <pthread.h>
#include <stdlib.h>

int prod[1]={0};
int n=6;
void *sum(void *args){
    int *a=(int *) args;
    int *result=malloc(sizeof(int));
    int s=1;
    for(int i=0;i<n;i++){
        s*=a[i];

    }
    printf("in thread product:%d\n",s);
    prod[0]=s;
    *result=s;
    return (void *) result;

    
}

int main(){
int* ans;
pthread_t p;
int ar[6]={1,2,3,4,5,6};
pthread_create(&p,NULL,&sum,ar);
pthread_join(p,(void**) &ans);

printf("product:%d\n",*ans);
free(ans);
}   

