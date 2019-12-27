

N, M = map(int, input().split())
matrix = [[0]*M]*N
for i in range(N):
    matrix[i] = [int(M) for M in input().split()]
#print (matrix)
S = str(input())


# N, M = 2, 3
# matrix = [[2,2,2],[2,2,2]]
# S = 'URDL'



while S:

    if S[:1] == 'U':
        for i in range(N-1):
            for j in range(M):
                #0詰め
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i+1][j]
                    matrix[i+1][j] = 0
                #合体発生
                if matrix[i][j] == matrix[i+1][j]:
                    matrix[i][j] *= 2
                    matrix[i+1][j] = 0

    elif S[:1] == "D":
        for i in reversed(range(N-1)):
            for j in range(M):
                #0詰め
                if matrix[i+1][j] == 0:
                    matrix[i+1][j] = matrix[i][j]
                    matrix[i][j] = 0
                #合体発生
                if matrix[i][j] == matrix[i+1][j]:
                    matrix[i][j] = 0
                    matrix[i+1][j] *= 2    
                
    elif S[:1] == "R":
        for i in range(N):
            for j in reversed(range(M-1)):
                #0詰め
                if matrix[i][j+1] == 0:
                    matrix[i][j+1] = matrix[i][j]
                    matrix[i][j] = 0
                #合体発生
                if matrix[i][j] == matrix[i][j+1]:
                    matrix[i][j] = 0
                    matrix[i][j+1] *= 2

    elif S[:1] == "L":
        for i in range(N):
            for j in range(M-1):
                #0詰め
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i][j+1]
                    matrix[i][j+1] = 0
                #合体発生
                if matrix[i][j] == matrix[i][j+1]:
                    matrix[i][j] *= 2
                    matrix[i][j+1] = 0
    S = S[1:]
    print(S[:1])
    for i in range(N):
        #print(matrix[i])
        #print('right : {:>3}'.format(matrix[i]))
        for j in range(M):
            print(matrix[i][j]),

    print('---')
print(matrix)
             

