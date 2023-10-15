def searchInsert(nums, target):
        i = 0
        j = len(nums)

        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return j

        # Binary search
        while i < j:
            mid = (i+j)//2

            if nums[mid] >= target and nums[mid-1] < target:
                break
            elif nums[mid] > target:   #move left side
                j = mid   
            else:
                i = mid +1
      
        return mid
            

        



n=list(map(int,input().split(",")))
val=int(input())
k=searchInsert(n,val)
print(k)