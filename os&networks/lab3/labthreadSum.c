#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int ar[1]={0};
const int n=5;
int arr[5]={1,2,3,4,5};
int s=0;

void *SumNumbers(void *args){
    int *a=(int *) args;
    for(int i=0;i<=n;i++){
        s=s+a[i];
    }
    int res=s;
    printf("Sum is %d\n",s);
    pthread_exit(res);
}
int main(){
    void *result;
    pthread_t pth;
    pthread_create(&pth,NULL,SumNumbers,arr);
    pthread_join(pth,&result);
    printf("Sum is %d\n",(int *) result);
}