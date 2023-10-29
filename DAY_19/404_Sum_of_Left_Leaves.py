def sumOfLeftLeaves(root):
    stack = [root]
    res = 0

    while stack:
        current = stack.pop()
        if current.left:
            if not current.left.left and not current.left.right:
                res += current.left.val
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return res  