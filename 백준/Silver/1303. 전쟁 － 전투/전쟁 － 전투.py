import sys
sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().strip().split())
war=[list(input().strip()) for _ in range(m)]
visited=[[False]*n for _ in range(m)]

dx=[1,0,-1,0]
dy=[0,-1,0,1]
W=0
B=0

def bfs(x,y):
    cnt=1
    queue = deque([(x,y)])
    visited[y][x]=True
    while queue:
        i,j=queue.popleft()
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if war[j][i]==war[ny][nx] and not visited[ny][nx]:
                    cnt+=1
                    visited[ny][nx]=True
                    queue.append((nx,ny))
    return cnt

for j in range(m):
    for i in range(n):
        if not visited[j][i]:
            k = bfs(i,j)
            if war[j][i]=="W":
                W+=k**2
            else:
                B+=k**2

print(W, B)