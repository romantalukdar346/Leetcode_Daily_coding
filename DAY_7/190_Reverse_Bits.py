def reverseBits(n):
        res=0
        for i in range(32):
            res= (res << 1 | n & 1)
            n>>= 1
        return res

n=int(input())
print(reverseBits(n))
        