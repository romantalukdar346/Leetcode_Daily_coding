def containsNearbyDuplicate(nums, k):
    visit={}
    for i,n in enumerate(nums):
        if n in visit and abs(i-visit[n])<=k:
            return True
        else:
            visit[n]=i
    return False
        



n= list(map(int,input().split(",")))
k=int(input())
print(containsNearbyDuplicate(n,k))