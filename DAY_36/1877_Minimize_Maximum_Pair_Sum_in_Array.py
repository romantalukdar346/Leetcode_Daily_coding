def minPairSum(self, nums):

    nums.sort()
    max_=0
    for i in range(len(nums)//2):
        max_=max(max_,(nums[i]+nums[-1-i]))
    return max_