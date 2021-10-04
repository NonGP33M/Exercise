#include <stdio.h>
int main() 
{
    int in;
    printf(" *** Show isosceles triangle ***\n");
    printf("Enter a counting number : ");
    scanf("%d",&in);
    if (in < 3)
        printf(" --- Incorrect number. ---");
    else
    {
        printf("Output :\n");
        for (int i = 1 ; i <= in ; i++)
        {
            for (int j = in ; j > i ; j--)
            {
                printf(" ");
            }

            for (int j = 1 ; j <= (i*2)-1 ; j++)
            {
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}