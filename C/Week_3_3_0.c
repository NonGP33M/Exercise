#include<stdio.h>
int main()
{
    int in,i,j,k;
    scanf("%d",&in);
    for (i = 1 ; i <= in ; i++)
    {
        if(i != in)
        {
            for (j = 1 ; j <= i ; j++)
            {
                printf("* ");
            }

            k = in - (2*(i-1)) + (in-3);
            for (j = 1 ; j <= k ; j++)
            {
                printf("  ");
            }

            for (j = 1 ; j <= i ; j++)
            {
                printf("* ");
            }

            printf("\n");
        }

        else
        {
            for (j = 1 ; j <= (2*in)-1 ; j++)
            {
                printf("* ");
            }

            printf("\n");
        }
    }

    for (i = in - 1 ; i > 0 ; i--)
    {
        for (j = 1 ; j <= i ; j++)
        {
            printf("* ");
        }

        k = in - (2*(i-1)) + (in-3);
        for (j = 1 ; j <= k ; j++)
        {
            printf("  ");
        }

        for (j = 1 ; j <= i ; j++)
        {
            printf("* ");
        }

        printf("\n");
    }
    return 0;
}
    

