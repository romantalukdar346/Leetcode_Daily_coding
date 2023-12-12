def totalMoney(self, n):
    
    #  1st solution
    total_money=0
    loop=0
    while n >0:
        if n>=7:
            loop+=1
            for i in range(7):
                total_money+=(i+loop)
            n-=7
        else:
            loop+=1
            for i in range(n):
                total_money+=(i+loop)
            n=0
    return total_money


    # 2nd solution
    # total_money=0
    # count=1
    # for i in range(1,n+1):
    #     if i%7==0:
    #         total_money+=count
    #         count= (i//7)+1
    #         continue
    #     total_money+=count
    #     count+=1
    # return total_money