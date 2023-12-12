def largestOddNumber(self, num):

    if int(num[-1])%2!=0:
        return num
    max_=0
    flag=0
    for i in range(len(num)-1,-1,-1):
        if int(num[i])%2!=0:
            max_=i
            flag=1
            break
    if not flag:
        return ''

    res=num[:max_+1]
    return res