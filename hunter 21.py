m,n=map(int,input().split())
matrix=[]
zero=[]
for i in range(n):
  zero.append(0)
matrix.append(zero)
#print(matrix)
for i in range(m):
  matrix.append(list(map(int,input().split()[:n])))
#print(matrix)
end_zero=[]
for i in range(n):
  end_zero.append(0)
matrix.append(end_zero)
#print(matrix)
for i in range(1,matrix):
  for j in range(0,n):
    if matrix[i][j]==0:
      for k in matrix[]
