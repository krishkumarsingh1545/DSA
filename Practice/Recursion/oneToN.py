def linear(n, count = 1):
    if count > n:
        return
    print(count)
    linear(n, count+1)

linear(4)
