count = 0

def numberOfInversions(nums):
    return mergeSort(arr, 0, len(arr)-1)

def mergeSort(arr: list, low, high) -> int:
    if low >= high:
        return;
    mid = (low + high)//2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    return count

def merge(arr:list, low, mid, high) -> list:
    global count
    left = low
    right = mid + 1
    arr2 = []
    while (left <= mid) and (right <= high):
        if arr[left] < arr[right]:
            arr2.append(arr[left])
            left+=1
        else:
            count += (mid - left + 1)
            arr2.append(arr[right])
            right+=1
    
    while left <= mid:
        arr2.append(arr[left])
        left+=1
    while right <= high:
        arr2.append(arr[right])
        right+=1
    for i in range(low, high+1):
        arr[i] = arr2[i - low]
    return arr

arr = [5,4,3,2,1]
print(arr)
mergeSort(arr, 0, len(arr)-1)
print(arr)
print(numberOfInversions(arr))