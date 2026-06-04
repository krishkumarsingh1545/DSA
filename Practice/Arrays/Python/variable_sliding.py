arr = [2, 4, 1, 7, 3, 6]
target = 10

L = 0
R = 0
min_length = float('inf')  # start with infinity (we want minimum)
current_sum = 0
i = 0
subb = arr[L:R]

while R < len(arr):
    print(current_sum)
    if current_sum < target:
        current_sum += arr[R]
        R+=1
    elif current_sum >= target:
        min_length = min(min_length, R - L)
        current_sum -= arr[L]
        L+=1

print(min_length)