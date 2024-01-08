def spiralOrder(self, matrix):
        
        row = len(matrix)
        col= len(matrix[0])
        fr,lr,fc,lc=0,row,0,col
        res=[]
        while fr<lr and fc< lc:
            for j in range(fc,lc):
                res.append(matrix[fr][j])
            
            for i in range(fr+1,lr):
                res.append(matrix[i][lc-1])

            if fr<lr-1:
                for j in range(lc-2,fc,-1):
                    res.append(matrix[lr-1][j])
            if fc < lc-1:
                for i in range(lr-1,fr,-1):
                    res.append(matrix[i][fc])
            fr+=1
            lr-=1
            fc+=1
            lc-=1
        return res