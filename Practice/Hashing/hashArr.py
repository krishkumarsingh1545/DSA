s = 'wfzdnbvov'
hashArr = [0] * 26

for i in s:
    hashArr[ord(i) - ord('a')]+=1

for i in range(len(hashArr)):
    if hashArr[i] != 0:
        print(f"{chr(i + ord('a'))}: {hashArr[i]}")