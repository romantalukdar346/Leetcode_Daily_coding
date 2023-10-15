def convertToTitle(columnNumber):
    result=''
    while columnNumber >0:
        c=chr(ord('A')+(columnNumber-1)%26)
        result=c+result
        columnNumber=(columnNumber-1)//26
    return result

columnNumber=int(input())
print(convertToTitle(columnNumber))