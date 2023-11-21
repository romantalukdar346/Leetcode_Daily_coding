def reductionOperations(self, nums):
    nums.sort()
    res=0
    lenght=len(nums)
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            res+=lenght-1-i
    return res