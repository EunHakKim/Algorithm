import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        d = nums[i][j]
        if d == 0:
            continue
        # 오른쪽 이동
        if j + d < n:
            dp[i][j + d] += dp[i][j]
        # 아래로 이동
        if i + d < n:
            dp[i + d][j] += dp[i][j]

print(dp[n - 1][n - 1])