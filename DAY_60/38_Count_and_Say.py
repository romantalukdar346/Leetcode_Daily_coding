def countAndSay(self, n):
    
    if n==1:
        return '1'
    if n==2:
        return '11'
    string='11'
    new_str=''
    n=n-2
    while n>0:
        count=1
        for i in range(1,len(string)):
            if string[i-1]==string[i]:
                count+=1
            else:
                new_str+=str(count)+string[-1]
                count=1
        new_str+=str(count)+string[-1]
        string=new_str
        new_str=''
        n-=1
    return string