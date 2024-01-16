def __init__(self):
        self.set_=list()

def insert(self, val):
    
    if val not in self.set_:
        self.set_.append(val)
        return True
    return False        

def remove(self, val):
    
    if val in self.set_:
        self.set_.remove(val)
        return True
    return False
    

def getRandom(self):
    import random
    len_=len(self.set_)
    inx=random.randint(0,len_-1)
    num= self.set_[inx]
    return num
