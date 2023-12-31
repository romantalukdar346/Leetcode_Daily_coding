def maxLengthBetweenEqualCharacters(self, s):
    from collections import defaultdict
    mapping=defaultdict(list)
    for i in range(len(s)):
        mapping[s[i]].append(i)
    max_=-1
    for val,count in mapping.items():
        if count!=1:
            st=mapping[val][0]+1
            end=mapping[val][-1]
            max_=max(max_,end-st)

    return max_