from collections import deque
import sys
input=sys.stdin.readline

M, N = map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(N)]
queue=deque([])
for i in range(M):
    for j in range(N):
        if tomato[j][i]==1:
            queue.append((i,j))

dx=[1,0,-1,0]
dy=[0,-1,0,1]

temp=1
for i in range(N):
    if 0 in tomato[i]:
        temp=0
if temp==1:
    print(0)
    exit()

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if tomato[ny][nx]==0:
                tomato[ny][nx]=tomato[y][x]+1
                queue.append((nx,ny))

for i in range(N):
    if 0 in tomato[i]:
        print(-1)
        exit()
print(max(map(max,tomato))-1)
