def swapPairs(self, head):
    def recur(node_odd):
        if node_odd is None:
            return node_odd

        node_even = node_odd.next
        if node_even == None:
            return node_odd                
        
        node_odd.next = recur(node_even.next)
        node_even.next = node_odd

        return node_even
    
    return (recur(head))

