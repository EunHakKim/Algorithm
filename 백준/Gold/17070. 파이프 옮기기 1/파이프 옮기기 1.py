import sys
input = sys.stdin.readline

n = int(input())
home = [[0 for _ in range(n)]]
for _ in range(n):
    home.append([*map(int, input().split())])

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n + 1)]
dp[1][1] = [1, 0, 0]

for i in range(1, n + 1):
    for j in range(1, n):
        if i == j == 1:
            continue
        if home[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if home[i - 1][j] == home[i][j - 1] == 0:
                dp[i][j][2] = sum(dp[i - 1][j - 1])
print(sum(dp[n][n - 1]))