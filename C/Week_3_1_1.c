#include<stdio.h>
#include<string.h>
int main()
{
    int sum = 0,i;
    char in[120];
    scanf("%s",&in);
    for ( i = 0 ; i < strlen(in) ; i++)
    {
        sum += in[i] - '0';
        if(sum > 9 && i == strlen(in) - 1)
        {
            sprintf(in,"%d",sum);
            sum = 0;
            i = -1;
        }
    }
    printf("%d",sum);
    return 0;
}