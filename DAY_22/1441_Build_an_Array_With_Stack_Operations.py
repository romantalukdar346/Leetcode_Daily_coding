def buildArray(target, n):
    oparetion=[]
    for i in range(1,n+1):
        if i in target:
            oparetion.append("Push")
        elif target[-1]>= i:
            oparetion.append("Push")
            oparetion.append("Pop")
        else:
            return oparetion
    return oparetion
