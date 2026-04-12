// 1 
// 0 1 
// 1 0 1 
// 0 1 0 1 
// 1 0 1 0 1
#include <stdio.h>
#include <stdlib.h>

int main() {
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j <= i; j++)
            printf("%d ", !((i+j)%2));
        printf("\n");        
    }
    return 0;
}