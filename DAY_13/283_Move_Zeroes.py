def moveZeroes(nums):
    k=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[k]=nums[i]
            k+=1
    for i in range(k,len(nums)):
        nums[k]=0
        k+=1
    return nums

# 2nd
    # a=len(nums)
    # nums[:] = [x for x in nums if x!= 0]
    # while len(nums)<a:
    #     nums.append(0)
    # return nums
# 3rd
    # for i in range(nums.count(0)):
    # nums.append(nums.pop(nums.index(0)))

# 4th
    # if len(nums)==1:
    #     return nums
    # k=len(nums)-1
    # for i in range(len(nums)-1,-1,-1):
    #     if nums[i]==0:  
    #         for j in range(i,k):
    #             nums[j]=nums[j+1]
    #         nums[k]=0
    #         k-=1
    # return nums


n=list(map(int,input().split(",")))
print(moveZeroes(n))