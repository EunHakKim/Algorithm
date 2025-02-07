import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
ans = 0

def dfs(x, y):
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(nx, ny)

for y in range(m):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            visited[y][x] = True
            dfs(x, y)
            ans += 1

print(ans)