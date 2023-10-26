def findTheDifference(s,t):
    # 1st solution
    for i in set(t):
        if t.count(i)>s.count(i):
            return i    
        
        
    # 2nd solution
    # if not s:
    #     return t[0]
    # t=Counter(t)
    # s=Counter(s)
    # for val,inx in t.items():
    #     if val not in s:
    #         return val
    #     elif val in s:
    #         if s[val]!= t[val]:
    #             return val 