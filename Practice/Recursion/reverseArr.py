def revArr(arr: list, l=0):
    r = len(arr) - 1 - l
    if l >= r : return
    arr[l], arr[r] = arr[r], arr[l]
    revArr(arr, l+1)

ll = [5, 3, 8, 53]
revArr(ll)
print(ll)