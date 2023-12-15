def numSpecial(self, mat):

    row=[0]*len(mat)
    col=[0]*len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                    row[i]+=1
                    col[j]+=1 
    ans=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                if row[i]==1 and col[j]==1:
                    ans+=1

    return ans