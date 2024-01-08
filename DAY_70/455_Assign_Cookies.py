def findContentChildren(self, g, s):
        
        count=0
        g.sort()
        s.sort()
        i,j=0,0
        n=len(s)
        m=len(g)
        while n> j and m > i:
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count