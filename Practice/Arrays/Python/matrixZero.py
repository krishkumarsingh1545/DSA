def setZeroes(matrix):
    hasharr = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                    hasharr.append([i, j])
    for k in hasharr:
        for i in range(len(matrix[k[0]])):
            matrix[k[0]][i] = 0
        for i in range(len(matrix)):
            matrix[i][k[1]] = 0
    print(matrix)


# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
                