def numberOfWays(self, corridor):
    num=corridor.count('S')
    mod=(10**9+7)
    if num%2==0 and num:
        pass
    else:
        return 0
    list_=[]
    counter=0
    ans=1
    flag=0
    for i in range(len(corridor)):
        if corridor[i]=='S':
            list_.append(i)
            counter+=1
            if counter % 2==0:
                flag=1
            else:
                if flag:
                    ans=ans * (list_[-1]-list_[-2])
                    flag=0
    return ans%mod