def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k =k+ 1
    return k


nums=list(map(int,input().split(",")))
k=removeDuplicates(nums)
print(k)
