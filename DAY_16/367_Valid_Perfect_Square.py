def isPerfectSquare( num):

    l=0
    h=num
    mid=0
    while l<=h:
        mid=(l+h)//2
        if mid*mid==num:
            return True
        elif mid*mid> num:
            h=mid-1
        else:
            l=mid+1
    return False