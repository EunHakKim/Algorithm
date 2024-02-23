N, K=map(int,input().split())

dp=[[0 for _ in range(K+1)]for _  in range(N+1)]

for i in range(N+1):
    for j in range(1,K+1):
        if j==1 or i==0:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]

print(dp[N][K]%1000000000)