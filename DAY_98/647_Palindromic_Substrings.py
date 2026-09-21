def countSubstrings(self, s):
    
    if len(s)==1:
        return 1
    count=len(s)
    res=[]
    self.dfs(s,0,2,res)
    return count+sum(res)

def dfs(self,s,st,end,res):
    if len(s)-1==st:
        return

    for j in range(st+end,len(s)+1):
        if s[st:j]==s[st:j][::-1]:
            res.append(1)
    
    self.dfs(s,st+1,end,res)