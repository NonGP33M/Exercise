#include<stdio.h>
int main()
{
    int sum = 0, i = 2, temp;
    while(i <= 10000)
    {
        for ( temp = 1 ; temp < i ; temp++)
        {
            if(i % temp == 0)
            {
                sum += temp;
            }
        }
        if(i == sum)
        {
            printf("%d\n",i);
        }
        sum = 0;
        i++;
    }
    return 0;
}