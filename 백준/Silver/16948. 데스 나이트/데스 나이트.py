import sys
from collections import deque
input = sys.stdin.readline

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[-1] * n for _ in range(n)]

queue = deque([(r1, c1)])
visited[r1][c1] = 0
while queue:
    r, c = queue.popleft()
    for d in range(6):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

print(visited[r2][c2])