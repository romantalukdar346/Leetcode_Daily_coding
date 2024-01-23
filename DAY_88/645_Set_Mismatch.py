def findErrorNums(self, nums):
    arr=[]
    n=len(nums)
    nums.sort()


    for i in range(1,len(nums)):
        if nums[i-1]==nums[i]:
            arr.insert(0,nums[i])
        elif nums[i-1]+1 < nums[i]:
            arr.append(nums[i-1]+1)

    if nums[0]!=1:
        arr.append(1)
    elif nums[n-1]!=n:
        arr.append(n)

    return arr  