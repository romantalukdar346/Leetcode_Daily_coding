def isPowerOfFour( n):
    import math
    if n<=0 : return False
    a = math.log(n,4)
    return a == int(a)


n=int(input())
print(isPowerOfFour(n))