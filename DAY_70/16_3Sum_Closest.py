def threeSumClosest(self, nums, target):
        
        diff=float('inf')
        sum_=0
        res=0

        nums.sort()
        n=len(nums)
        start,end,nxt=0,n-1,1

        while start < n-2:
            
            while nxt < n-1 and end!=nxt:

                min_=0
                sum_=nums[start]+nums[nxt]+nums[end]
                min_=abs(target-sum_)

                if sum_ < target:
                    nxt+=1
                elif sum_ > target:
                    end-=1
                else:
                    return sum_

                if diff> min_:
                    res=sum_
                    diff=min_
            start+=1
            nxt=start+1
            end=n-1

        return res