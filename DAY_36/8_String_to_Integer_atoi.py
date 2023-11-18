def myAtoi(self, s):

    s=s.strip()
    if not len(s):
        return 0
    sigh=1
    if s[0]=='-':
        sigh=-1
        s=s[1:]
    elif s[0]=='+':
        s=s[1:]
    i,num=0,0
    while i<len(s) and s[i].isdigit():
        num=num*10+int(s[i])
        i+=1
    return max(min(num*sigh,2**31-1),-2**31)