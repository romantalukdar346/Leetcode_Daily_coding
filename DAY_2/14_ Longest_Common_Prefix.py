def longestCommonPrefix(strs):
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        ans=""
        for i in range(len(first)):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans

m=int(input())
n=[]
for i in range(m):
    n.append(input())
res=longestCommonPrefix(n)
print(res)