import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
ans = 0

def back(x, y, depth):
    global ans
    if depth == k and x == c - 1 and y == 0:
        ans += 1
        return
    elif x == c - 1 and y == 0:
        return
    elif depth >= k:
        return
    
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0<=nx<c and 0<=ny<r:
            if not visited[ny][nx] and graph[ny][nx] != 'T':
                visited[ny][nx] = True
                back(nx, ny, depth + 1)
                visited[ny][nx] = False

visited[r - 1][0] = True
back(0, r - 1, 1)

print(ans)