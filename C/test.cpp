#include<stdio.h>

int main()
{
    int size,i,j,out;
    scanf("%d",&size);
    for (i = 0 ; i < size ; i++)
    {
        out = 122 - i;
        for (j = 0 ; j < size ; j++)
        {
            printf("%c",out);
            out--;
        }
        printf("\n");
    }
    return  0;
}