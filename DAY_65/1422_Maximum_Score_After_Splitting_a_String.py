def maxScore(self, s):
    # 1st solution
    max_=0
    zeros=0
    ones=0
    zeros,ones=s[0].count('0'),s[1:].count('1')
    max_=zeros+ones
    for i in range(1,len(s)-1):
        if s[i]=='0':
            zeros+=1
        elif s[i]=='1':
            ones-=1
        
        max_=max(max_,zeros+ones)
    return max_

    # 2nd solution
    # max_=0
    # max_=max(max_,s[0].count('0')+s[1:].count('1'))
    # for i in range(1,len(s)-1):
    #     max_=max(max_,s[:i+1].count('0')+s[i+1:].count('1'))
    # return max_