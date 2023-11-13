def longestPalindrome(self, s):

    if len(s)==1:
        return 1
    lentgh=0
    look=set(s)
    odd=0
    for key in look:
        value=s.count(key)
        if value%2==0:
            lentgh+=value
        else:
            odd=1
            lentgh+=value-1

    return lentgh+odd