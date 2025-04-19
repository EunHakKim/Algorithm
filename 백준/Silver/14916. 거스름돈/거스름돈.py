n = int(input())

dp = [0] * 100001
dp[:10] = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]

for i in range(10, n + 1):
    dp[i] = min(dp[i - 5] + 1, dp[i - 2] + 1)

print(dp[n])