def threeSum(self, nums):
    nums.sort()
    target=0
    s=set()
    output=[]
    for i in range(len(nums)):
        j=i+1
        k=len(nums)-1
        while j<k:
            add= nums[i]+nums[j]+nums[k]
            if add==target:
                s.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
            elif add > target:
                k-=1
            else:
                j+=1
    output=list(s)
    return output