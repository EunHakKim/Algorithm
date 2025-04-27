import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[False] * (m + 1) for _ in range(n)]
if s - v[0] >= 0:
    dp[0][s - v[0]] = True
if s + v[0] <= m:
    dp[0][s + v[0]] = True

for i in range(1, n):
    for j in range(m + 1):
        if j - v[i] >= 0 and dp[i - 1][j]:
            dp[i][j - v[i]] = True
        if j + v[i] <= m and dp[i - 1][j]:
            dp[i][j + v[i]] = True

ans = -1
for i in range(m + 1):
    if dp[-1][i]:
        ans = i
print(ans)