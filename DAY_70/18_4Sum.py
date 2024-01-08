def fourSum(self, nums, target):
        
        res=[]
        nums.sort()
        n=len(nums)
        sum_=0

        for start in range(len(nums)):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            for nxt in range(start+1,len(nums)):
                if nxt > start+1 and nums[nxt] == nums[nxt-1]:
                    continue
                end=n-1
                mid=nxt+1
                while mid < end:
                    
                    sum_=nums[start]+nums[nxt]+nums[mid]+nums[end]
                    if sum_==target:                            
                        res.append([nums[start],nums[nxt],nums[mid],nums[end]])
                        while mid < end and nums[mid] == nums[mid+1]:
                            mid += 1
                        while mid < end and nums[end] == nums[end-1]:
                            end -= 1
                        mid+=1
                        end-=1
                    elif sum_ >target:
                        end-=1
                    elif sum_ < target:
                        mid+=1
        return res