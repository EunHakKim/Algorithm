T=int(input())

for i in range(T):
    n=int(input())
    dp=[]
    dp.append(list(map(int, input().split())))
    dp.append(list(map(int, input().split())))
    for k in range(1,n):
        if k==1:
            dp[0][k]+=dp[1][0]
            dp[1][k]+=dp[0][0]
        else:
            dp[0][k]+=max(dp[1][k-1], dp[1][k-2])
            dp[1][k]+=max(dp[0][k-1], dp[0][k-2])
    print(max(dp[0][n-1],dp[1][n-1]))