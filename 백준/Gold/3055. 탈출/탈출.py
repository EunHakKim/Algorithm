import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]
go, end = None, None
water = set([])

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            go = (j, i)
            graph[i][j] = '.'
            visited[i][j] = 0
        elif graph[i][j] == '*':
            water.add((j, i))
        elif graph[i][j] == 'D':
            end = (j, i)

queue = deque([go])
while True:
    # 물이 확장
    new_water = set([])
    for x, y in water:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r:
                if graph[ny][nx] == '.':
                    graph[ny][nx] = '*'
                    new_water.add((nx, ny))
    water = new_water

    # 고슴도치 이동
    new_queue = deque([])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r:
                if visited[ny][nx] == -1 and (graph[ny][nx] == '.' or graph[ny][nx] == 'D'):
                    visited[ny][nx] = visited[y][x] + 1
                    new_queue.append((nx, ny))
    queue = new_queue

    # 탈출 처리
    if len(queue) == 0:
        break

if visited[end[1]][end[0]] == -1:
    print("KAKTUS")
else:
    print(visited[end[1]][end[0]])