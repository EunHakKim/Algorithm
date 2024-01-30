N=int(input())

dp=[[0 for i in range(N)] for _ in range(10)]

for i in range(10):
    dp[i][0]=1

for i in range(N-1):
    for j in range(10):
        sum=0
        for k in range(j+1):
            sum+=dp[k][i]
        dp[j][i+1]=sum%10007

result=0
for i in range(10):
    result+=dp[i][N-1]

print(result%10007)
