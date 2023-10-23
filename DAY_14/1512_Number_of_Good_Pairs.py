def numIdenticalPairs(nums):
    nums.sort()
    current=-1
    count=[]
    for i in range(len(nums)):
        if nums[i]!=current:
            current=nums[i]
            count.append(nums.count(nums[i]))
    pair=0
    for i in count:
        if i>=2:
            pair+=i*(i-1)//2
    return pair

n=list(map(int,input().split(",")))
print(numIdenticalPairs(n))

    # pair=0
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]==nums[j]:
    #             pair+=1
    # return pair


    # pair=0
    # j=-1
    # nums.sort()
    # for i in nums:
    #     if j!= i:
    #         j=i
    #         count=nums.count(i)
    #         if count>=2:
    #             pair+=count*(count-1)/2
    # return int(pair)


