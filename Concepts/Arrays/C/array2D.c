#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[3][4] = {{3, 23, 54, 43},
                     {2, 25, 78, 458},
                     {32, 40, 23, 64}};

    int sizeX = sizeof(arr)/sizeof(arr[0]);
    int sizeY = sizeof(arr[0])/sizeof(int);
    for (int i = 0; i < sizeX; i++)
    {
        for (int j = 0; j < sizeY; j++)
            printf("%d\t", arr[i][j]);
        printf("\n");
    }
    return 0;
}