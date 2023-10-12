def removeElement(nums, val):

    # list comprehension

    # new_arr=[i for i in nums if i!=val]
    # return len(new_arr)

    # index tracking
    
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


n=list(map(int,input().split(",")))
val=int(input())
k=removeElement(n,val)
print(k)