def transpose(self, matrix):
    # 1st solution
    new_matrix=[]
    for i in range(len(matrix[0])):
        n_m=[]
        for j in range(len(matrix)):
            n_m.append(matrix[j][i])
        new_matrix.append(n_m)

    return new_matrix

    # 2nd solution
    # import numpy as np
    # matrix=np.array(matrix)
    # return matrix.T