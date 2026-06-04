nums = [2,0,2,1,1,0]
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    hasharr = [0, 0, 0]
    for i in nums:
        hasharr[i]+=1
    nums = []
    for i in range(len(hasharr)):
        for j in range(hasharr[i]):
            nums.append(i)
    print(nums)

sortColors(nums)