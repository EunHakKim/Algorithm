import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
shark = []
ans = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            shark.append((x, y))
            graph[y][x] = 0
        else:
            graph[y][x] = sys.maxsize

for x, y in shark:
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] > graph[cy][cx] + 1:
                    graph[ny][nx] = graph[cy][cx] + 1
                    queue.append((nx, ny))

for y in range(n):
    ans = max(ans, max(graph[y]))
print(ans)