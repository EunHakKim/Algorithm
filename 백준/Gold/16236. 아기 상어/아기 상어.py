import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
shark = ()
visited = [[-1]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))
    if 9 in graph[i]:
        shark = (graph[i].index(9), i)
size = 2
stack = 0
time = 0
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs():
    global time
    global shark
    x,y=shark
    graph[y][x]=0
    visited[y][x]=0
    queue = deque([shark])
    ans = []
    temp = sys.maxsize
    while queue:
        x, y = queue.popleft()
        if visited[y][x]==temp:
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if visited[ny][nx]==-1:
                    if graph[ny][nx]==size or graph[ny][nx]==0:
                        visited[ny][nx]=visited[y][x]+1
                        queue.append((nx,ny))
                    elif graph[ny][nx]!=0 and graph[ny][nx]<size:
                        visited[ny][nx]=visited[y][x]+1
                        ans.append((ny,nx))
                        if temp == sys.maxsize:
                            temp = visited[ny][nx]
    if temp==sys.maxsize:
        return False
    ans.sort()
    time += temp
    y, x=ans[0]
    shark = (x,y)
    return True


while True:
    visited = [[-1]*n for _ in range(n)]
    if not bfs():
        print(time)
        exit()
    stack += 1
    if stack==size:
        stack=0
        size+=1
    
