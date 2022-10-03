X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[11,12,13],
    [14,15,16],
    [17,18,19]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for k in range(len(X[0])):
       result[i][k] = X[i][k] * Y[i][k]
for r in result:
   print(r)