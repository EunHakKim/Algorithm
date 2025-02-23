import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(x, y):
    if visited[y][x]:
        return visited[y][x]
    
    visited[y][x] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if forest[ny][nx] > forest[y][x]:
                visited[y][x] = max(visited[y][x], dfs(nx, ny) + 1)
    return visited[y][x]

for i in range(n):
    for j in range(n):
        if not visited[j][i]:
            dfs(i, j)

print(max(map(max, visited)))