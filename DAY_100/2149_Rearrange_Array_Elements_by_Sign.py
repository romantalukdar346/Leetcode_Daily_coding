def rearrangeArray(self, nums):

    res=[0]*len(nums)
    i,j=0,1
    for inx ,val in enumerate(nums):
        if val>0:
            res[i]=val
            i+=2
        else:
            res[j]=val
            j+=2
    return res