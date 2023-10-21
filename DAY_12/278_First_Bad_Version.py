def firstBadVersion(n):
        start,end=1,n
        bad=1
        
        while start<=end:
            mid=(end+start)//2
            if isBadVersion(mid):
                end=mid-1
                bad=mid
            else:
                start=mid+1
        return bad
n=int(input())
print(firstBadVersion(n))