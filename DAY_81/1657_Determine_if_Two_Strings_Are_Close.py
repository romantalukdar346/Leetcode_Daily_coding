def closeStrings(self, word1, word2):
        from collections import Counter
        if len(word1)!=len(word2):
            return False
        if len(set(word1))!=len(set(word2)):
            return False

        s_w1=set(word1)
        s_w2=set(word2)

        for val in s_w1:
            if val not in s_w2:
                return False
        
        w1=Counter(word1)
        w2=Counter(word2)
        
        w_1=[]
        w_2=[]

        for val in w1.values():
            w_1.append(val)

        for val in w2.values():
            w_2.append(val)
        w_1.sort()
        w_2.sort()

        for i in range(len(w_1)):
            if w_1[i]!=w_2[i]:
                return False
        return True