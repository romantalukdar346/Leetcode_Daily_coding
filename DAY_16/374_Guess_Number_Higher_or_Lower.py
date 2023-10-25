def guessNumber(n):
    l=1
    while l<=n:
        mid=(l+n)//2
        res=guess(mid)
        if  res<0:
            n=mid-1
        elif res>0:
            l=mid+1
        else:
            return mid
