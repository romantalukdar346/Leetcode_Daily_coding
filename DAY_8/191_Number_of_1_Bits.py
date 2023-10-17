def hammingWeight(n):
    count=0
    for i in range(32):
        if n & (1<<i):
            count+=1
    return count






n=int(input())
print(hammingWeight(n))
