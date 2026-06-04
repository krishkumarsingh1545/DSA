arr = [2, 4, 1, 7, 3, 6]
# Find the largest sum of any 3 consecutive numbers

# size = 6
# slide = 4
# window size = 3
max = 0
for i in range((len(arr)-3)+1):
    temp = 0
    print("i: ", i)
    for j in range(i, i+3):
        print(j, arr[j])
        temp += arr[j]
    if temp > max:
        max = temp

print(max)
