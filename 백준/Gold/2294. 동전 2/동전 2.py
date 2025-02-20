import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []
dp = [-1] * 100001
for _ in range(n):
    value = int(input())
    values.append(value)
    dp[value] = 1

for i in range(k + 1):
    for value in values:
        if i - value > 0:
            if dp[i - value] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i - value] + 1
                else:
                    dp[i] = min(dp[i], dp[i - value] + 1)

print(dp[k])