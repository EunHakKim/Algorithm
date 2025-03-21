import sys
input = sys.stdin.readline

m, n = map(int, input().split())
nums = [list(input()) for _ in range(m)]
dp = [[] for _ in range(m)]
for i in range(m):
    for j in range(n):
        dp[i].append(int(nums[i][j]))

for i in range(1, m):
    for j in range(1, n):
        if dp[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

ans = 0
for arr in dp:
    temp = max(arr)
    ans = max(ans, temp)
print(ans ** 2)