import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(3)]
dp = [[[0] * (len(arr[2]) + 1) for _ in range(len(arr[1]) + 1)] for _ in range(len(arr[0]) + 1)]
ans = 0

for i in range(1, len(arr[0]) + 1):
    for j in range(1, len(arr[1]) + 1):
        for k in range(1, len(arr[2]) + 1):
            if arr[0][i - 1] == arr[1][j - 1] and arr[1][j - 1] == arr[2][k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k - 1], dp[i][j - 1][k], dp[i - 1][j][k])

for i in range(1, len(arr[0]) + 1):
    for j in range(1, len(arr[1]) + 1):
        for k in range(1, len(arr[2]) + 1):
            ans = max(ans, dp[i][j][k])

print(ans)