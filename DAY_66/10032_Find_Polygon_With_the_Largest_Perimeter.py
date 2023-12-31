def largestPerimeter(self, nums):
    
    nums.sort()
    add=0
    for i in nums:
        add+=i
    for i in range(len(nums)-1,-1,-1):
        add-=nums[i]
        if add > nums[i]:
            if (len(nums) == i+1 )or  (len(nums[:i+1])>=3):
                
                return add+nums[i]
    return -1
        