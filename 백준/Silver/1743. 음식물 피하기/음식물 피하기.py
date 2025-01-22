from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
eumsseu = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0

for _ in range(k):
    r, c = map(int, input().split())
    eumsseu[r - 1][c - 1] = True

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = dx[k] + cx
            ny = dy[k] + cy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and eumsseu[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and eumsseu[i][j]:
            s = bfs(i, j)
            ans = max(ans, s)

print(ans)