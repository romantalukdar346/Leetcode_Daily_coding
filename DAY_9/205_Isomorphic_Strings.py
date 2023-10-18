def isIsomorphic(s, t):
    # if len(s) != len(t):
    #     return False
    # if len(set(s))!= len(set(t)):
    #     return False
    
    visit={}
    for i in range(len(s)):
        if s[i] not in visit:
            if t[i] in visit.values():
                return False
            visit[s[i]]=t[i]
        else:
            if visit[s[i]]==t[i]:
                continue
            else:
                return False
    return True





str1=input()
str2=input()
print(isIsomorphic(str1,str2))
