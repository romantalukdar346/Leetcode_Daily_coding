from collections import Counter
def findMode( root):
        s=[]
        s.append(root)
        l=[]
        while s:
            c=s.pop()
            if c.left:
                s.append(c.left)
            if c.right:
                s.append(c.right)
            
            l.append(c.val)
        count=Counter(l)
        max_val= max(count.values())
        mode=[key for key,value in count.items() if value ==max_val]
        return mode