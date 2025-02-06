import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = []
dp = [0] * (k + 1)
for _ in range(n):
    items.append(tuple(map(int, input().split())))

for w, v in items:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
print(dp[k])