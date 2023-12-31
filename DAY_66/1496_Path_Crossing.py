def isPathCrossing(self, path):
    
    mapping= []
    x,y=0,0
    mapping.append([0,0])
    for value in path:
        if value=='N':
            y+=1
        elif value=='E':
            x+=1
        elif value=='S':
            y-=1
        else:
            x-=1
        if [x,y] in mapping:
            return True
        mapping.append([x,y])
    return False