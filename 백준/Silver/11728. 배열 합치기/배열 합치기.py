import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

a.sort()
b.sort()

p = 0
for i in range(n):
    while p < m and a[i] > b[p]:
        ans.append(b[p])
        p += 1
    ans.append(a[i])

while p < m:
    ans.append(b[p])
    p += 1

print(*ans)