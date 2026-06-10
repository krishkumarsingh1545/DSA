def linear(n):
    if n < 1:
        return
    print(n)
    linear(n-1)

linear(4)
