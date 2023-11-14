def sortVowels(self, s):
    import heapq
    vowel='AEIOUaeiou'
    ascii_=[]
    heapq.heapify(ascii_)
    v_index=[]

    for i in range(len(s)):
        if s[i] in vowel:
            v_index.append(i)
            heapq.heappush(ascii_,ord(s[i]))

    s_list=list(s)

    for i in v_index:
        s_list[i]=chr(heapq.heappop(ascii_))
    return "".join(s_list)