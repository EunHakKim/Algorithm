N=int(input())

sum=[[0,0,1],
     [0,1,1],
     [0,1,2],
     [0,1,2],
     [0,1,2],
     [0,1,2],
     [0,1,2],
     [0,1,2],
     [0,1,2],
     [0,1,1]]

for i in range(3,N+1):
    sum[0].append((sum[1][i-1])%1000000000)
    for j in range(1,9):
        sum[j].append((sum[j-1][i-1]+sum[j+1][i-1])%1000000000)
    sum[9].append((sum[8][i-1])%1000000000)

result=0
for i in range(10):
    result+=sum[i][N]

print(result%1000000000)