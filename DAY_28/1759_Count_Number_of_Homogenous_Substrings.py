def countHomogenous(self, s):
    count=1
    res=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            res+=(count*(count+1))/2
            count=1
    res+=(count*(count+1))/2
    return res%(10**9+7)