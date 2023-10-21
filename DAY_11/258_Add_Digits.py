def addDigits(num):
    
    if num <=9:
        return num
    else:
        n=num
        sum=0
        while n>9:
            sum=0
            while n>0:
                sum+=n%10
                n//=10
            n=sum
        return sum

    # if num==0 : return 0
    # if num%9==0: return 9
    # else: return num%9


n=int(input())
print(addDigits(n))
