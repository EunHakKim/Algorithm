import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
two = ()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(m):
        if arr[j]==1:
            arr[j]=-1
        elif arr[j]==2:
            two=(j, i)
    graph.append(arr)

def bfs():
    two_x, two_y = two
    graph[two_y][two_x] = 0
    queue = deque([two])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx]==-1:
                    graph[ny][nx] = graph[y][x]+1
                    queue.append((nx, ny))
bfs()
for eachrow in graph:
    print(*eachrow)
