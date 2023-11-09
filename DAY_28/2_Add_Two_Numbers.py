def addTwoNumbers(self, l1, l2):
    start=ListNode(0)
    temp=start
    carry=0
    while l1 is not None or l2 is not None or carry!=0:

        val1= l1.val if l1 is not None else 0
        val2= l2.val if l2 is not None else 0

        sum=val1+val2+carry
        digit=sum%10
        carry=sum//10

        newnode=ListNode(digit)
        temp.next=newnode
        temp=temp.next

        l1=l1.next if l1 is not None else None
        l2=l2.next if l2 is not None else None 

    return start.next