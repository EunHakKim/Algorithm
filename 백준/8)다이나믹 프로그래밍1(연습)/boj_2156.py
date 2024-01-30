n=int(input())
dp=[[int(input())for _ in range(n)],[]]
for x in dp[0]:
    dp[1].append(x)

for i in range(1,n):
    if i==1:
        dp[0][i]+=0
        dp[1][i]+=dp[0][i-1]
    elif i==2:
        dp[0][i]+=max(dp[0][i-2],dp[1][i-2])
        dp[1][i]+=dp[0][i-1]
    else:
        dp[0][i]+=max(dp[0][i-2],dp[1][i-2],dp[0][i-3],dp[1][i-3])
        dp[1][i]+=dp[0][i-1]

max0=max(dp[0])
max1=max(dp[1])
print(max(max0,max1))