arr = [7, 54, 3, 9, 65, 11, 89]

def bubbleSort(arr):
    for i in range(len(arr), -1, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print('Before selection sort: ', arr)
print('After selection sort: ', bubbleSort(arr))