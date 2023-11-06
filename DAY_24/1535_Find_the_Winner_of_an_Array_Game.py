def getWinner(self, arr, k):
    if k>=len(arr):
        return max(arr)
    map={}
    while True:
        temp=max(arr[0],arr[1])
        arr.append(arr.remove(min(arr[0],arr[1])))

        if temp not in map:
            map[temp]=1
        else:
            map[temp]+=1

        if map[temp]==k:
            return temp
        
        