def firstPalindrome(self, words):
    for inx, val in enumerate(words):
        n=len(val)
        if n%2==0:
            f=val[:n//2]
            l=val[n//2:][::-1]
            if f==l:
                return val
        else:
            f=val[:n//2]
            l=val[n//2+1:][::-1]
            if f==l:
                return val
    return ''