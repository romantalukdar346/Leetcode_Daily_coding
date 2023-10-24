class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
    
        # nums2=set(nums2)

        # inter=[]
        # for i in nums2:
        #     if i in nums1:
        #         inter.append(i)
         
        # return inter

n1=list(map(int,input().split(",")))
n2=list(map(int,input().split(",")))
print(Solution().intersection(n1,n2))
