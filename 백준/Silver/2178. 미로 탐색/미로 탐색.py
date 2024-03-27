from collections import deque
import sys
input=sys.stdin.readline

N, M = map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]
queue=deque([(0,0)])

dx=[1,0,-1,0]
dy=[0,-1,0,1]
cnt=0
    
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1

print(graph[N-1][M-1])