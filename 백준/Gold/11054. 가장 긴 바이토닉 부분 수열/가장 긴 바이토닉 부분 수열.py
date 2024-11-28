import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

a.reverse()
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()

ans = 0
for i in range(n):
    ans = max(ans, dp1[i] + dp2[i] - 1)
print(ans)