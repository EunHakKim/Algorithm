import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
treasure = [list(input().strip()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
ans = 0

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = 0
    cx, cy = x, y
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if visited[ny][nx] == -1 and treasure[ny][nx] == 'L':
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[cy][cx] + 1
    return visited[cy][cx]

for i in range(n):
    for j in range(m):
        if treasure[i][j] == 'L':
            visited = [[-1] * m for _ in range(n)]
            ans = max(ans, bfs(j, i))

print(ans)