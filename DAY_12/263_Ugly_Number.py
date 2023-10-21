def isUgly( n):
    
    if n<=0:
        return False
    for i in [2,3,5]:
        while n%i==0:
            n//=i
    return n==1









    # if n<=0:
    #     return False
    # if n==1:
    #     return True
    # if n%2==0 or n%3==0 or n%5==0:
    #     flag=0
    #     for i in range(7,n+1):
    #         if n%i==0:
    #             for j in range(2,(i+1)//2):
    #                 if i%j==0:
    #                     flag=1
    #                     break
    #             if flag==0:
    #                 return False
    #             flag=0
            
    #     return True
    # else:
    #     return False
    
n=int(input())
print(isUgly(n))