arr: list = [3, 23, 54, 43 ,2, 25, 78, 458, 23, 64]

for i in range(len(arr)-1):
    arr[i+1]+=arr[i]
    print(arr[i], end=' ')
print(arr[len(arr)-1])