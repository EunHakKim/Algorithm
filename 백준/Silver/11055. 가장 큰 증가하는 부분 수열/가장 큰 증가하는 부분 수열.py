import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [x for x in a]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j] + a[i], dp[i])

print(max(dp))
