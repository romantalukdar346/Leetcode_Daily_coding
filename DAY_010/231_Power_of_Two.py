def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n-1 )) == 0    


n=int(input())
print(isPowerOfTwo(n))