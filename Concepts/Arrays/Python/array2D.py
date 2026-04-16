arr: list = [[3, 23, 54, 43], [2, 25, 78, 458], [32, 40, 23, 64]]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()