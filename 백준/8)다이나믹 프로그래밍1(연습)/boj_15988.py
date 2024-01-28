T=int(input())

dp=[0,1,2,4]

for _ in range(T):
    n=int(input())
    if n<len(dp):
        print(dp[n])
        continue
    for i in range(len(dp),n+1):
        dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000009)
    print(dp[n])