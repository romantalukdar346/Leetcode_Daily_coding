def largestGoodInteger(self, num):
    count=1
    max_=0
    flag=0
    for i in range(1,len(num)):
        if num[i]==num[i-1]:
            count+=1
        else:
            count=1
        if count==3:
            flag=1
            max_=max(int(num[i]),max_)
    if not flag:
        return ""
    return str(max_)*3