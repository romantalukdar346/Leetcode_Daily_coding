def longestPalindrome(self, s):
    from collections import defaultdict
    if len(s)==1:
        return s
    seen=defaultdict(list)

    for inx, value in enumerate(s):
        seen[value].append(inx)
    s_set=set(s)
    max_=0
    res=''
    for char in s_set:
        if len(seen[char])>1:
            inx=seen[char]
            point=0
            for i in inx:
                point+=1
                for j in inx[point:]:
                    palindrome=str(s[i:j]+s[j])
                    temp=palindrome[::-1]
                    if temp==palindrome and max_< len(temp):
                        res=temp
                        max_=len(temp)
    if len(s)>1 and not res:
        return s[0]
    return res