N=int(input())

dp=[0 for _ in range(31)]
dp[2]=3

for i in range(4,31):
    if i%2!=0:
        continue
    dp[i]+=2
    temp=i
    while temp>0:
        temp-=2
        if i-temp==2:    
            dp[i]+=dp[temp]*3
        else:
            dp[i]+=dp[temp]*2

print(dp[N])