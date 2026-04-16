arr: list = [3, 23, 54, 43 ,2, 25, 78, 458, 23, 64]

left, right = 0, len(arr)-1

print("Before Swap: ", arr, end=" ")

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
    
print()
print("After Swap: ", arr, end=" ")