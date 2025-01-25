import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
scnt, wcnt, sans, wans = 0, 0, 0, 0

def dfs(x, y):
    global scnt, wcnt
    if graph[y][x] == 'v':
        wcnt += 1
    elif graph[y][x] == 'o':
        scnt += 1
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<c and 0<=ny<r:
            if not visited[ny][nx] and graph[ny][nx] != '#':
                visited[ny][nx] = True
                dfs(nx, ny)

for x in range(c):
    for y in range(r):
        if not visited[y][x] and graph[y][x] != '#':
            scnt, wcnt = 0, 0
            visited[y][x] = True
            dfs(x, y)
            if scnt > wcnt:
                sans += scnt
            else:
                wans += wcnt
        
print(sans, wans)