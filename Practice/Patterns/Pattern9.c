//     *
//    ***
//   *****
//  *******
// *********
// *********
//  *******
//   *****
//    ***
//     *
#include <stdio.h>
#include <stdlib.h>

int main() {
    for (int i = 0; i < 5; i++)
    {
        for (int k = 4-i; k > 0; k--)
        {
            printf(" ");
        }
        for (int j = 0; j <= 2*i; j++) {
            printf("*");
        }
        printf("\n");              
    }
    for (int i = 0; i < 5; i++)
    {
        for (int k = 0; k < i; k++)
        {
            printf(" ");
        }
        for (int j = 10; j > i*2+1; j--) {
            printf("*");
        }
        printf("\n");        
    }
    return 0;
}