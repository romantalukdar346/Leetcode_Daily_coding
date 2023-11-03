class Solution(object):
    def help(self,root,res):
        if  root:
            self.help(root.left,res)
            res.append(root.val)
            self.help(root.right,res)

    def inorderTraversal(self, root):
        res=[]
        self.help(root,res)
        return res