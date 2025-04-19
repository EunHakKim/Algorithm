import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
vans, kans = 0, 0

def bfs(x, y):
    global vans, kans
    vcnt, kcnt = 0, 0
    if graph[x][y] == 'v':
        vcnt += 1
    elif graph[x][y] == 'k':
        kcnt += 1
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 1 <= nx < r - 1 and 1 <= ny < c - 1:
                if not visited[nx][ny]:
                    if graph[nx][ny] == '#':
                        continue
                    elif graph[nx][ny] == 'v':
                        vcnt += 1
                    elif graph[nx][ny] == 'k':
                        kcnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    if vcnt >= kcnt:
        vans += vcnt
    else:
        kans += kcnt

for j in range(1, r - 1):
    for i in range(1, c - 1):
        if not visited[j][i] and graph[j][i] != '#':
            bfs(j, i)

print(kans, vans)