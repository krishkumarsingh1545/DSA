#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[10] = {3, 23, 54, 43 ,2, 25, 78, 458, 23, 64};
    int size = sizeof(arr)/sizeof(int);
    for (int i = 0; i < size; i++)
    {
        printf("%d\t", arr[i]);
    }
    
    return 0;
}