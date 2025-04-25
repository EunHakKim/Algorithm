import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ice = [0] * 1000001
current = 0
for _ in range(n):
    g, x = map(int, input().split())
    ice[x] = g

if 2 * k >= 1000000:
    print(sum(ice))
    exit()

for i in range(2 * k + 1):
    current += ice[i]

ans = current
for i in range(1000000 - 2 * k):
    current -= ice[i]
    current += ice[i + 2 * k + 1]

    ans = max(ans, current)

print(ans)