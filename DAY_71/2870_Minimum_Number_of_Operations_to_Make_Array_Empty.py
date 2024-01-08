def minOperations(self, nums):
    from collections import Counter
    ss=set(nums)
    nums=Counter(nums)
    res=0
    print(nums)
    for val in ss:
        loop=1
        th_c=0

        while loop:
            if nums[val]==0:
                loop=0
            elif nums[val]-3 >=0:
                th_c+=1
                nums[val]-=3
                res+=1
            else:
                if nums[val]==2:
                    nums[val]-=2
                    res+=1
                elif th_c:
                    th_c-=1
                    res+=1
                    nums[val]=0
                else:
                    return -1
    return res