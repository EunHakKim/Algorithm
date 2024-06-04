import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dist = [[-1]*M for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

queue = deque()
queue.append((0,0))
dist[0][0]=0
while queue:
    x,y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<M and 0<=ny<N:
            if dist[ny][nx]==-1:
                if graph[ny][nx]==0:
                    dist[ny][nx]=dist[y][x]
                    queue.appendleft((nx,ny))
                else:
                    dist[ny][nx]=dist[y][x]+1
                    queue.append((nx,ny))

print(dist[N-1][M-1])