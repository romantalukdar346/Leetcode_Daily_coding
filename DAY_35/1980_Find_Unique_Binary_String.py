def findDifferentBinaryString(self, nums):
    max_n=2**len(nums[0])
    seen={}
    binary=''
    for i in nums:
        seen[int(i,2)]=1
    for j in range(max_n):
        if j not in seen:
            binary=bin(j)[2:]
            break
            
    binary="0"*(len(nums[0])-len(binary))+binary
    return binary
