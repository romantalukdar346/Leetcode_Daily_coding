def maxProductDifference(self, nums):
    
    max_1=max(nums)
    nums.remove(max_1)

    max_2=max(nums)
    nums.remove(max_2)

    min_1=min(nums)
    nums.remove(min_1)

    min_2=min(nums)
    nums.remove(min_2)

    return (max_1*max_2)-(min_1*min_2)