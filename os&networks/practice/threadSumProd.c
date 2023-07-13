#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <wait.h>
#include <unistd.h>

struct arguments{
    int f;
    int s;
};
void *SumProd(void *ptr){
    struct arguments *ptrargs=(struct arguments*)ptr;
    int a=ptrargs->f;
    int b=ptrargs->s;
    int *result=malloc(sizeof(int));
    *result=a*b;
    return (void ** ) result;
}
int main(){
    pthread_t thread;
    int *res;
    struct arguments args;
    int c,d;
    scanf("%d",&c);
    scanf("%d",&d);
    args.f=c;
    args.s=d;
    pthread_create(&thread,NULL,SumProd,(void *) &args);
    pthread_join(thread,(void **) &res);
    printf("Product:%d\n",*res);


}