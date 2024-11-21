import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = mars[0][0]

for i in range(1, m):
    dp[0][i] = dp[0][i -1] + mars[0][i]

for i in range(1, n):
    arr = []
    for j in range(m):
        dp[i][j] = dp[i - 1][j] + mars[i][j]
        arr.append(dp[i][j])

    for j in range(1, m):
        dp[i][j] = max(dp[i][j], dp[i][j - 1] + mars[i][j])

    for j in range(m - 2, -1, -1):
        arr[j] = max(arr[j], arr[j + 1] + mars[i][j])

    for j in range(m):
        dp[i][j] = max(dp[i][j], arr[j])

print(dp[n - 1][m - 1])