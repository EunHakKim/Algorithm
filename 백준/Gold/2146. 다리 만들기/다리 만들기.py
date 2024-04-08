from collections import deque
import sys
input=sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
num = 1
res = int(1e9)

def bfs(i,j):
  dx=[1,0,-1,0]
  dy=[0,-1,0,1]
  que = deque()
  que.append([i,j])
  while que:
    x, y = que.popleft()
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]
      if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny]:
        visited[nx][ny] = 1
        graph[nx][ny] = num
        que.append([nx,ny])

def bfs2(index):
  dx=[1,0,-1,0]
  dy=[0,-1,0,1]
  queue = deque()
  dist = [[-1]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if graph[i][j]==index:
        dist[i][j] = 0
        queue.append([i,j])

  while queue:
    x, y = queue.popleft()
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]
      if 0<=nx<N and 0<=ny<N:
        if graph[nx][ny] and graph[nx][ny]!=index:
          return dist[x][y]
        elif (not graph[nx][ny]) and dist[nx][ny]==-1:
          dist[nx][ny] = dist[x][y]+1
          queue.append([nx,ny])

  return int(1e9)

for i in range(N):
  for j in range(N):
    if graph[i][j] and not visited[i][j]:
      visited[i][j] = 1
      graph[i][j] = num
      bfs(i,j)
      num += 1

for index in range(1,num):
  res = min(res, bfs2(index))
print(res)