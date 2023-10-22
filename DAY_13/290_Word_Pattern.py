def wordPattern(pattern, s):
        if (len(pattern)!=len(s.split())):
            return False
        map={}
        s=s.split()
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if s[i] not in map.values():
                    map[pattern[i]]=s[i]
                else:
                    return False               
            elif map[pattern[i]]!=s[i]:
                return False
        return True


str1=input()
str2=input()
print(wordPattern(str1,str2))