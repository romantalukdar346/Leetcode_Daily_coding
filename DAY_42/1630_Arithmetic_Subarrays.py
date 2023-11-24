def checkArithmeticSubarrays(self, nums, l, r):
    ans=[]
    for i in range(len(l)):
        start=l[i]
        stop=r[i]
        if stop== len(nums)-1:
            sort_=nums[start:]
        else:
            sort_=nums[start:stop+1]
        sort_.sort()
        ans.append(self.ArithmeticSubarray(sort_))
    return ans
    
def ArithmeticSubarray(self,arr):
    diff=arr[1]-arr[0]
    for i in range(2,len(arr)):
        if (arr[i]-arr[i-1])==diff:
            continue
        else:
            return False
    return True