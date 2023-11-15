def maximumElementAfterDecrementingAndRearranging(self, arr):


    arr.sort()
    temp=0
    for i in range(len(arr)):
        if arr[i]>=temp+1:
            arr[i]=temp+1
            temp+=1

    return arr[-1]