def uniqueOccurrences(self, arr):
        
        mapping={}
        for val in arr:
            if val not in mapping:
                mapping[val]=1
            else:
                mapping[val]+=1

        Aset=[val for val in mapping.values()]
        if len(Aset)==len(set(Aset)):
            return True
        return False