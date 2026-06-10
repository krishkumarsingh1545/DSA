def names(name, count = 0):
    if not count < 5:
        return
    print(name)
    count+=1
    names(name, count)

names('Krish')