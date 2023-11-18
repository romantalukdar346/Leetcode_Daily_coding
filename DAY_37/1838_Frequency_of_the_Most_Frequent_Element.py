def maxFrequency(self, nums, k):

    nums.sort()
    left=0
    ans=0
    curr_sum=0

    for right in range(len(nums)):
        curr_sum+=nums[right]

        if (curr_sum +k) < nums[right]*(right-left+1):
            curr_sum-=nums[left]
            left+=1
        ans=max(ans,(right-left+1))
    return ans