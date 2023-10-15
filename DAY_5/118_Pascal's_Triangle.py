def generate(numRows):
    if numRows==1:
        return [[1]]
    elif numRows==2:
        return [[1],[1,1]]
    else:
        res=[[1],[1,1]]
        for i in range(numRows-2):
            temp=[1]
            for j in range(len(res[-1])-1):
                temp.append(res[-1][j]+res[-1][j+1])
            temp.append(1)
            res.append(temp)
        return res


n=int(input())
print(generate(n))