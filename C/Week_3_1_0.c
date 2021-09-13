#include<stdio.h>
int main()
{
    int in,temp,sum = 0;
    scanf("%d",&in);
    while (in != 0)
    {
        temp = in % 10;
        sum += temp;
        in = in / 10;
        if(sum > 9 && in < 1)
        {
            in = sum;
            sum = 0;
        }
    }
    
    printf("%d",sum);
    return 0;
}