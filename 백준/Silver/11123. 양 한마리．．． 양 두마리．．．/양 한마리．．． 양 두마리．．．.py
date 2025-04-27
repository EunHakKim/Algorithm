import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(t):
    h, w = map(int, input().split())
    g = [list(input().strip()) for __ in range(h)]
    visited = [[False] * w for __ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and g[i][j] == '#':
                visited[i][j] = True
                ans += 1
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < w and 0 <= ny < h:
                            if not visited[ny][nx] and g[ny][nx] == '#':
                                visited[ny][nx] = True
                                queue.append((ny, nx))

    print(ans)