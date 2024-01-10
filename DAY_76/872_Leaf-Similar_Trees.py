def leafSimilar(self, root1, root2):
        
        arr1=[]
        arr2=[]
        self.dfs(root1,arr1)
        self.dfs(root2,arr2)
        if arr1==arr2:
            return True
        return False

def dfs(self,root,arr):
    if not root:
        return
    if not root.left and not root.right:
        arr.append(root.val)
    self.dfs(root.left,arr)
    self.dfs(root.right,arr)