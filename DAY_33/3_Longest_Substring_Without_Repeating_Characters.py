def lengthOfLongestSubstring(self, s):
    if not s:
        return 0
    if len(s)==1:
        return 1
    max_res=0
    res=0
    s_list=[]
    
    for value in s:
        if value not in s_list:
            s_list.append(value)
        else:
            res=len(s_list)
            inx=s_list.index(value)
            s_list=s_list[inx+1:]
            max_res=max(max_res,res)
            s_list.append(value)

    res=len(s_list)
    max_res=max(max_res,res)
    return max_res