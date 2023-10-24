def reverseVowels(s):
        
        v=""
        a=""
        b=-1
        for i in s:
            if(i in "aeiouAEIOU"):
                v+=str(i)
        # m=v[::-1]
        for i in s:
            if(i not in "aeiouAEIOU"):
                a+=str(i)
        #print(a)
            else:
                a+=v[b]
        #print(a)
                b-=1
        #print(a)
        return a
 
        # map='aeiouAEIOU'
        # l=0
        # r=len(s)-1
        # s_list=list(s)
        # while l < r:
        #     while l < r and map.find(s_list[l])==-1:
        #         l+=1
        #     while l < r and map.find(s_list[r])==-1:
        #         r-=1
        #     s_list[l],s_list[r]=s_list[r],s_list[l]
        #     r-=1
        #     l+=1
        # return "".join(s_list)



n=input()
print(reverseVowels(n))