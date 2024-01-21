def dfs(self,matrix,path,res,row,col,n):
    
    if row<0 or col <0 or col==n:
        return
    if n-1 == row:
        res.append(path+matrix[row][col])
        return
    

    path+=matrix[row][col]
    self.dfs(matrix,path,res,row+1,col,n)
    self.dfs(matrix,path,res,row+1,col-1,n)
    self.dfs(matrix,path,res,row+1,col+1,n)

def minFallingPathSum(self, matrix):
    n=len(matrix)
    row,col=0,0
    res=[]
    sum_=0
    for i in range(n):
        self.dfs(matrix,sum_,res,row,i,n)
    print(res)
    return min(res)
