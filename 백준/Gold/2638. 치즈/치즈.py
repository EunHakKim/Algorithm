import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

while True:
    # 전체 녹음 체크
    temp = False
    for arr in graph:
        if 1 in arr:
            temp = True
    if not temp:
        break

    ans += 1
    visited = [[False] * m for _ in range(n)]
    cheese = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    # 접촉 체크
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]:
                    if graph[ny][nx] == 1: # 외부 공기와 접촉
                        cheese[ny][nx] += 1
                    else:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

    # 녹음 처리
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 2:
                graph[i][j] = 0

print(ans)
# 2변이상 외부와 접촉 -> 녹음
# 치즈 내부에 있는 공간 -> 외부 공기와 접촉하지 않는 것으로 가정
# 외부 공기를 bfs -> 치즈와 접촉 -> 접촉 배열 +1 -> 녹음 처리