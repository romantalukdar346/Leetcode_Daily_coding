def strStr(haystack, needle):
        
        return haystack.find(needle)



        # flag=0
        # j=0
        # index=0
        # for i in range(len(haystack)):
        #     if haystack[i]==needle[j] and j<=len(needle)-1:
        #         if flag==0:
        #             index=i
        #             flag=1
        #         if j==len(needle)-1 and flag==1:
        #             return index
        #         j+=1
        #     else:
        #         flag=0
        #         index=0
        #         j=0
        # return -1





needle=input()
haystack=input()
k=strStr(needle,haystack)
print(k)