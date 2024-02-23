n=int(input())
dp=[]

for i in range(n):
    nums=list(map(int,input().split()))
    dp.append(nums)

for i in range(1,n):
    for j in range(i+1):
        if i==1:
            dp[i][j]+=dp[0][0]
        elif j==0:
            dp[i][j]+=dp[i-1][j]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])
        
print(max(dp[n-1]))