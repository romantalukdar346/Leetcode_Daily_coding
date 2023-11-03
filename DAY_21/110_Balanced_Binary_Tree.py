def isBalanced(root):
        if not root:
            return True
        if abs(self.rotation(root.right)-self.rotation(root.left))<2 and self.isBalanced(root.right) and self.isBalanced(root.left):
            return True
        else:
            return False
def rotation(self,root):
        if not root:
            return 0
        return 1+max(self.rotation(root.left),self.rotation(root.right))