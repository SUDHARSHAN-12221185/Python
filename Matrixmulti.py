arr=[[4,5,7,3],[8,9,2,4],[2,3,5,9]]
arr1=[[4,1],[2,2],[8,7],[9,7]]
t=len(arr)
M=[[0 for i in range(len(arr1[0]))] for k in range(len(arr))]
for i in range(len(arr)):
    for j in range(len(arr1[0])):
        for k in range(len(arr[0]) or len(arr1)):
            M[i][j]+=arr[i][k]*arr1[k][j]
for i in range(len(arr)):
    for j in range(len(arr1[0])):
        print(M[i][j],end=" ")
    print()