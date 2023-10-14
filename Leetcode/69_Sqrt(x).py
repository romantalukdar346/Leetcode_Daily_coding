def mySqrt(x):
    if x <2:
        return x
        
    low = 0
    high = x
    while abs(low-high) != 1:
        mid = (low+high) // 2
        if mid*mid == x:
            return mid

        if mid*mid > x:
            high = mid
        else:
            low = mid
    
    return low
            

n= int(input())
print(mySqrt(n))
        