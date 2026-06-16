arr = [7, 54, 3, 9, 65, 11, 89]

def selectionSort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]: min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr
    
print('Before selection sort: ', arr)
print('After selection sort: ', selectionSort(arr))