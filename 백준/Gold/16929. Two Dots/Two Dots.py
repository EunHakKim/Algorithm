N, M = map(int,input().split())

graph = [list(map(str,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dfs(x,y,depth):
    visited[y][x]=depth
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if depth > 3:
                if visited[ny][nx]==1:
                    print("Yes")
                    exit()
            if visited[ny][nx]==0 and graph[y][x]==graph[ny][nx]:
                dfs(nx,ny,depth+1)
                visited[ny][nx]=0
    visited[y][x]=0

for i in range(M):
    for j in range(N):
        dfs(i,j,1)
print("No")