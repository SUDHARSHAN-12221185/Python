arr=[[4,5,7,3],
     [8,9,2,4],
     [2,3,5,9]]
arr2=[[4,1],
      [2,7],
      [8,7],
      [9,7]]
T=len(arr)
M=[[0 for i in range(T)] for k in range(T)]
for i in range(T):
    for j in range(T):
        for k in range(T):
            M[i][j]+=arr[i][k]*arr[k][j]
for i in range(T):
    for j in range(T):
        print(M[i][j],end=' ')
    print()