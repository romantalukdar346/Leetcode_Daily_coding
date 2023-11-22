def findDiagonalOrder(self, nums):
# 1st solution

    from collections import defaultdict
    res=defaultdict(list)
    for row in range(len(nums)-1,-1,-1):
        for col in range(len(nums[row])):
            res[row+col].append(nums[row][col])
    ans=[]
    curr=0

    while curr in res:
        ans.extend(res[curr])
        curr+=1
    return ans


# 2nd solution
    # res=[]
    # row,col=0,0
    # res.append(nums[row][col])
    # j=1
    # max_col= max(len(inner) for inner in nums)
    # while  row < len(nums) - 1 or col < max_col - 1:

    #     for i in range(row-1,-1,-1):
    #         try:
    #             res.append(nums[i][j])
    #         except IndexError:
    #             pass
            
    #         j+=1
        
    #     if row < len(nums)-1:
    #         row+=1
    #         res.append(nums[row][col])
    #         j=1
    #     else:
    #         col+=1
    #         try:
    #             res.append(nums[row][col])
    #         except IndexError:
    #             pass
    #         j=col+1
    # return res
