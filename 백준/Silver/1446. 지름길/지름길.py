import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dp = {}
dp[0] = 0
dp[d] = d
roads = []
for i in range(n):
    a, b, c = map(int, input().split())
    if 0 <= a <= d and 0 <= b <= d:
        if b - a > c:
            dp[a] = a
            dp[b] = b
            roads.append((a, b, c))
roads.sort()

for a, b, c in roads:
    if dp[a] + c < dp[b]:
        dp[b] = dp[a] + c
        for k in dp.keys():
            if k > b:
                if dp[b] + k - b < dp[k]:
                    dp[k] = dp[b] + k - b

print(dp[d])