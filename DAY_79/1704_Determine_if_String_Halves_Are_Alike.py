def halvesAreAlike(self, s):
        
        vowels ='aeiouAEIOU'
        l=len(s)
        n=(l/2)
        s1=s[:n]
        s2=s[n:]
        l1,l2=0,0
        for i in range(n):
            if s1[i] in vowels:
                l1+=1
            if s2[i] in vowels:
                l2+=1
        if l1==l2:
            return True
        return False