def postorderTraversal(self, root):
    res=[]
    self.post(root,res)
    return res

def post(self,root,res):
    if not root:
        return
    self.post(root.left,res)
    self.post(root.right,res)
    res.append(root.val)