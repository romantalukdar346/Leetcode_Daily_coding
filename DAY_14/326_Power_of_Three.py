def isPowerOfThree(n):
    # 1st
    # return n>0 and 3**19 % n==0

    # 2nd
    import math
    power=round(math.log(n)/math.log(3))

    # 3rd
    # power=round((math.log(n,3)),1).is_integer()
    
    if 3**power==n:
        return True
    else:
        return False

n=int(input())
print(isPowerOfThree(n))

