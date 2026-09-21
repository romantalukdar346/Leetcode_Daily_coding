def numberOfBeams(self, bank):
    
    beam=[]
    count=0
    for i in range(len(bank)):
        count=bank[i].count('1')
        if count>0:
            beam.append(count)
        count=0
    res=0
    for i in range(1,len(beam)):
        res+=beam[i]*beam[i-1]
    return res