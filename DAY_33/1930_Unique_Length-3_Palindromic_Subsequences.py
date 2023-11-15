from collections import defaultdict
#1st solution
class Solution(object):
    def countPalindromicSubsequence(self, s):
        u = set(s)
        count  = 0
        for c in u:
            i1 = s.find(c)
            i2 = s.rfind(c)
            if i2>i1:
                count += len(set(s[i1+1:i2]))

        return count

#2nd solution
# class Solution(object):
#     def countPalindromicSubsequence(self, s):
#         d=defaultdict(list)
#         for i,c in enumerate(s):
#             d[c].append(i)
#         ans=0
#         for el in d:
#             if len(d[el])<2:
#                 continue
#             a=d[el][0]
#             b=d[el][-1]
#             ans+=len(set(s[a+1:b]))
#         return(ans)
    

		
		