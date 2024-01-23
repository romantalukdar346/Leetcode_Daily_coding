def maxLength(self, arr):
    res=[]

    for inx in range(len(arr)):
        self.dfs(arr,inx,res,'')
    return max(res)

def dfs(self,arr,inx,res,string):
    if len(arr)<=inx:
        res.append(len(string))
        return

    temp=''
    temp=string+arr[inx]
    if len(temp)==len(set(temp)):
        string+=arr[inx]

    self.dfs(arr,inx+1,res,string)
    for j in range(2,len(arr)-inx):
        self.dfs(arr,inx+j,res,string)
    

