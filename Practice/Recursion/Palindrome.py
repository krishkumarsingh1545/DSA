def chk(s, i = 0):
    j = len(s) - 1 - i
    if i >= len(s)-1//2: return True
    if (s[i] != s[j]):
        return False
    return chk(s, i+1)
    # return True

print(chk('racecar'))
    