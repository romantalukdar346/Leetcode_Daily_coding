def countNodes(self, root):
    if not root:
        return 0
    res=[]
    res.append(root)
    count=1
    loop=True
    while loop:
        node=res.pop(0)

        if node.left:
            res.append(node.left)
            count+=1

            if node.right:
                res.append(node.right)
                count+=1

            else:
                loop=False 
        else:
            loop=False
    return count

# 2nd solution
    # if not root:
    #     return 0
    # left, right = root, root
    # layer = 0
    # while left and right:
    #     layer += 1
    #     left = left.left
    #     right = right.right
    # if not left and not right:
    #     return 2 ** layer - 1
    # return 1 + self.countNodes(root.left) + self.countNodes(root.right)