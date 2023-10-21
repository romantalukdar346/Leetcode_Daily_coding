def isAnagram(s, t):
        if len(s)!=len(t):
            return False
        mapping={}
        for i in s:
            if i not in mapping:
                mapping[i]=1
            else:
                mapping[i]+=1
        for i in t:
            if i in mapping:
                mapping[i]-=1
            else:
                return False
        for i in mapping.values():
            if i!=0:
                return False
            else:
                return True

        # return sorted(s)==sorted(t)




str1=input()
str2=input()
print(isAnagram(str1,str2))