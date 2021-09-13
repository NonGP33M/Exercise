#include<stdio.h>
main(){

    int A;
    int i;
    int j;
    scanf("%d",&A);
    for(i = 1;i <= A;i++){
        for(j = 1;j <= 2*A-1;j++){
            if(j > A-i && j <= A+(i-1)){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }

    for(i = A-1;i >= 1;i--){
        for(j = 1;j <= 2*A-1;j++){
            if(j > A-i && j <= A+(i-1)){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
}