import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[0])
    exit()

dp = [[0, x, x] for x in stairs]
dp[0] = [0, stairs[0], stairs[0]]
dp[1] = [stairs[0], stairs[1], stairs[0] + stairs[1]]

for i in range(2, n):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i - 1][0] + stairs[i]
    dp[i][2] = dp[i - 1][1] + stairs[i]

print(max(dp[n - 1][1], dp[n - 1][2]))