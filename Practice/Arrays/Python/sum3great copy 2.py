arr = [2, 4, 1, 7, 3, 6]
arr = [9, 1, 1, 1, 1, 1]
# Find the largest sum of any 3 consecutive numbers

# size = 6
# slide = 4
# window size = 3

winSize = int(input('Enter the window size: '))
temp = sum(arr[:winSize])
max = temp
for i in range((len(arr)-winSize)):
    print(i)
    temp -= arr[i]
    temp += arr[i+winSize]
    if temp > max:
        max = temp

print(max)
