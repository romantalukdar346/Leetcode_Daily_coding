def rangeSumBST(self, root, low, high):
        
        res=[]
        self.dfs(root,res,low,high)
        return sum(res)

def dfs(self,root,res,low,high):
    if not root:
        return
    if root.val>=low and root.val<= high:
        res.append(root.val)
    self.dfs(root.left,res,low,high)
    self.dfs(root.right,res,low,high)