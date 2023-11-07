# 1st Solution
class Solution(object):
    def __init__(self):
        self.counter=0
    def averageOfSubtree(self, root):
        if not root:
            return
        self.dfs(root)
        self.averageOfSubtree(root.left)
        self.averageOfSubtree(root.right)
        return self.counter

    def dfs(self,root):
        stack=[]
        val=0
        total_node=0
        if root:
            stack.append(root)
        while stack:
            total_node+=1
            node=stack.pop(0)
            val+=node.val

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if (val//total_node)==root.val:
            self.counter+=1


# 2nd Solution (Better one)
# class Solution(object):
#     def __init__(self):
#         self.counter=0
#     def averageOfSubtree(self, root):
#         if not root:
#             return
#         self.sum_and_node_count(root)
#         return self.counter

#     def sum_and_node_count(self,root):
#         if not root:
#             return 0,0

#         left_total,total_left_node=self.sum_and_node_count(root.left)
#         right_total,total_right_node=self.sum_and_node_count(root.right)

#         total_sum=right_total+left_total+root.val
#         total_node=total_left_node+total_right_node+1

#         if (total_sum//total_node)==root.val:
#             self.counter+=1
#         return total_sum, total_node

            
            

        
        