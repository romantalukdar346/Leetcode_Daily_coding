def sequentialDigits(self, low, high):
    
    res=[]
    string='12345678999'
    n=len(str(low))
    m=n
    f=0

    while int(string[f:f+n])< low:
        if int(string[f:f+n])>123456789:
            return res
        f+=1
        
    num=int(string[f:f+n])
    n+=f
    i=f
    while high>=num:
        i+=1
        if n<=9:
            res.append(num)
            n+=1
            num=int(string[i:n])
        elif len(str(high))>=m+1:
            m+=1
            num=int(string[:m])
            n,i=m,0

        if num>123456789:
            return res
    return res