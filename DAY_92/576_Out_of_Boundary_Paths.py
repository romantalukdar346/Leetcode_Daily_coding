def findPaths(self, m, n, maxMove, startRow, startColumn):
    return self.dfs(startRow,startColumn,maxMove,m,n) % (10**9+7)

def dfs(self,row,col,max_,m,n):

    if max_<0:
        return 0
    if row <0 or row>=m or col<0 or col>=n:
        return 1
    a=self.dfs(row-1,col,max_-1,m,n)
    b=self.dfs(row+1,col,max_-1,m,n)
    c=self.dfs(row,col-1,max_-1,m,n)
    d=self.dfs(row,col+1,max_-1,m,n)

    return a+b+c+d