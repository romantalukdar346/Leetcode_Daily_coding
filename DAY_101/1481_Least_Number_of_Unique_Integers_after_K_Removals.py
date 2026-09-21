def findLeastNumOfUniqueInts(self, arr, k):
    
    m={}
    for i in range(len(arr)):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1


    m=sorted(m.values())
    n=len(m)

    for i in range(len(m)):
        if m[i]<=k:
            n-=1
            k-=m[i]
        else:
            break
    return n