def isHappy(n):
    visit=[]
    if n==1:
        return True
    while n not in visit:
        visit.append(n)
        string=str(n)
        n=0
        for i in string:
            n=n+int(i)**2

        if n==1:
            return True
    return False


n= int(input())
print(isHappy(n))
