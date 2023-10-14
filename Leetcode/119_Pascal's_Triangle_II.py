def getRow(rowIndex):
    triangle=[[1]]
    for i in range(1,rowIndex+1):
        temp=[1]
        for j in range(1,i):
            temp.append(triangle[i-1][j]+triangle[i-1][j-1])
        temp.append(1)
        triangle.append(temp)
    return triangle[rowIndex]



n= int(input())
print(getRow(n))
