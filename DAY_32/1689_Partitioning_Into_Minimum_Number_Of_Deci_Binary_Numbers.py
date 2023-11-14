def minPartitions(self, n):
    max_=0
    for i in range(9,-1,-1):
        if str(i) in n:
            return i