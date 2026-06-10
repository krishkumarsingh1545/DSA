def linear(n):
    if n < 1:
        return
    linear(n-1)
    print(n)

linear(4)
