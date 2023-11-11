def getIntersectionNode(self, headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA
    node1=headA
    node2=headB
    while node1 is not  node2:
        node1= node1.next if node1 is not None else headB
        node2= node2.next if node2 is not None else headA
    return node1