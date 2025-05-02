import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [sys.maxsize] * 150001
visited[n] = 0
ans = 0
queue = deque([n])

while queue:
    cx = queue.popleft()
    if cx == k:
        ans += 1

    if cx + 1 <= 150000 and visited[cx + 1] >= visited[cx] + 1:
        visited[cx + 1] = visited[cx] + 1
        queue.append(cx + 1)
    if cx - 1 >= 0 and visited[cx - 1] >= visited[cx] + 1:
        visited[cx - 1] = visited[cx] + 1
        queue.append(cx - 1)
    if 2 * cx <= 150000 and visited[2 * cx] >= visited[cx] + 1:
        visited[2 * cx] = visited[cx] + 1
        queue.append(2 * cx)

print(visited[k])
print(ans)

# 걷기 -> 1초 후에 x - 1, x + 1
# 순간이동 -> 1초 후에 2 * x