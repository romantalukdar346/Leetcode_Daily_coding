def makeEqual(self, words):
        total_len = 0
        for word in words:
            total_len += len(word)
        if total_len % len(words) != 0:
            return False


        mapping={}
        for value in words:
            for ch in value:
                if ch not in mapping:
                    mapping[ch]=1
                else:
                    mapping[ch]+=1
        
        
        n=len(words)
        for count in mapping.values():
            if count%n!=0:
                return False
        return True