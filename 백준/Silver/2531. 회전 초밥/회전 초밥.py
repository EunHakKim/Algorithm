import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
susi = [int(input()) for _ in range(n)]

visited = [0] * 3001
temp = 0

for i in range(k):
    if visited[susi[i]] == 0:
        visited[susi[i]] += 1
        temp += 1
    else:
        visited[susi[i]] += 1


if visited[c] == 0:
    temp += 1
    visited[c] += 1
else:
    visited[c] += 1

l, r = 0, k - 1
ans = temp

while True:
    visited[susi[l]] -= 1
    if visited[susi[l]] == 0:
        temp -= 1
    
    l = (l + 1) % n
    r = (r + 1) % n
    
    if visited[susi[r]] == 0:
        temp += 1
    visited[susi[r]] += 1

    ans = max(ans, temp)

    if l == 0:
        break

print(ans)
