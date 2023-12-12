def tree2str(self, root):
    if not root:
        return ""
    if  not root.left and  not root.right:
        return str(root.val)
    
    res=[]
    res.append(str(root.val))
    
    if not root.left:
        res.append("()")
    self.help(root.left,res)
    self.help(root.right,res)

    return "".join(res)

def help(self,root,res):
    if root:
        res.append('(')
        res.append(str(root.val))

        if root.left:
            self.help(root.left,res)
        elif root.right:
            res.append("()")
            self.help(root.right,res)

        if root.left and root.right:
            self.help(root.right,res)

        res.append(")")
    return