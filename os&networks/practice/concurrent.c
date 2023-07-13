#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <wait.h>

void func(int arr[],int n){
    pid_t a;
    int sum=0;
    int p=1;
    a=fork();
    for(int i=0;i<n;i++){
        if(a==0){
            sum+=arr[i];
            printf("Sum:%d\n",sum);
            sleep(1);
        }
        else if(a>1){
            p*=arr[i];
            printf("product:%d\n",p);
            sleep(1);

        }
    }

   printf("Parent Calculated Product %d \n Child Calculated sum %d\n",p,sum);

}
int main(){
    int arr[6]={1,2,3,4,5,6};
    func(arr,6);
    return 0;
}