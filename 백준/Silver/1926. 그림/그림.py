import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt, ans = 0, 0

def bfs(x, y):
    visited[y][x] = True
    queue = deque([(x, y)])
    w = 1
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and painting[ny][nx] == 1:
                    w += 1
                    visited[ny][nx] = True
                    queue.append((nx, ny))
    return w

for i in range(n):
    for j in range(m):
        if not visited[i][j] and painting[i][j] == 1:
            cnt += 1
            ans = max(ans, bfs(j, i))

print(cnt)
print(ans)