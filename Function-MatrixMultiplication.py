def matrix_multiplication(A,B):
  res = [[0 for x in range(2)] for y in range(2)] 
  for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j] += A[i][k] * B[k][j]  
  return(res)

A1 = [[12,7],
        [4 ,5]]
B1 = [[5,8],
        [6,7]]
print(matrix_multiplication(A1,B1))

