def maxCoins(self, piles):

    res=0
    piles.sort()
    n=len(piles)//3
    j=-2
    for i in range(n):
        res+=piles[j]
        j-=2
    return res