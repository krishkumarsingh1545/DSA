// *
// **
// ***
// ****
// *****
// ****
// ***
// **
// *
#include <stdio.h>
#include <stdlib.h>

int main() {
    for (int i = 0; i < 10; i++)
    {
        if (i < 5)
        {
            for (int j = 0; j < i; j++)
                printf("*");
        }
        if (i >= 5)
        {
            for (int j = 5; j > i%5; j--)
                printf("*");
        }
        printf("\n");        
    }
    return 0;
}