N=int(input())
dp=[[0,1],[0,2]]

for i in range(1,N+1):
    dp[0].append((dp[0][i]+dp[1][i])%9901)
    dp[1].append((2*dp[0][i]+dp[1][i])%9901)

print((dp[0][N]+dp[1][N])%9901)