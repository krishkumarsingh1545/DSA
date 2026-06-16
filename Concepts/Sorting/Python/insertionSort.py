arr = [7, 54, 3, 9, 65, 11, 89]

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print('Before selection sort: ', arr)
print('After selection sort: ', insertionSort(arr))