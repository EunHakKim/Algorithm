import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[[-1] * m for _ in range(n)] for __ in range(2)]

# bfs 시작
visited[0][0][0] = 1
queue = deque([(0, 0, 0)]) # 마지막에 벽을 부술 수 있는지 여부를 담아줌
while queue:
    x, y, can_crack = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if visited[can_crack][ny][nx] == -1:
                if graph[ny][nx] == 0: # 가능한 길을 찾아 이동
                    visited[can_crack][ny][nx] = visited[can_crack][y][x] + 1
                    queue.append((nx, ny, can_crack))
                else: # 벽을 부수고 이동
                    if can_crack == 0:
                        visited[1][ny][nx] = visited[0][y][x] + 1
                        queue.append((nx, ny, 1))

if visited[0][n - 1][m - 1] == -1:
    print(visited[1][n - 1][m - 1])
elif visited[1][n - 1][m - 1] == -1:
    print(visited[0][n - 1][m - 1])
else:
    print(min(visited[0][n - 1][m - 1], visited[1][n - 1][m - 1]))