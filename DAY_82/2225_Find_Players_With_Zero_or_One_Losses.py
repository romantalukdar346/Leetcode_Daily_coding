def findWinners(self, matches):
        
        s_lose=set()
        s_participate=set()
        mapping={}

        for val in matches:
            s_participate.add(val[0])
            if val[1] not in mapping:
                s_participate.add(val[1])
                s_lose.add(val[1])
                mapping[val[1]]=1
            else:
                mapping[val[1]]+=1
        win_=[i for i in s_participate if i not in s_lose]
        lose_=[i for i in s_lose if mapping[i]==1]
        
        return [sorted(win_),sorted(lose_)]