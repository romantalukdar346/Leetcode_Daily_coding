def pseudoPalindromicPaths (self, root):
    return self.dfs(root,0)
def dfs(self,root,cnt):
    if not root: return 0
    cnt ^= 1 << (root.val - 1)
    if root.left is None and root.right is None:
        return 1 if cnt & (cnt - 1) == 0 else 0
    return self.dfs(root.left, cnt) + self.dfs(root.right, cnt)