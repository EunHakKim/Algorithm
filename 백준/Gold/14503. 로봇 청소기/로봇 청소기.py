import sys
input = sys.stdin.readline

n, m = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
cnt=0

while True:
    if graph[r][c]==0 and not visited[r][c]:
        visited[r][c]=True
        cnt+=1
        continue
    clean=False
    for i in range(4):
        nx = c + dx[i]
        ny = r + dy[i]
        if graph[ny][nx]==0 and not visited[ny][nx]:
            clean=True
    if not clean:
        if d==0:
            if graph[r+1][c]==1:
                break
            else:
                r+=1
        elif d==1:
            if graph[r][c-1]==1:
                break
            else:
                c-=1
        elif d==2:
            if graph[r-1][c]==1:
                break
            else:
                r-=1
        else:
            if graph[r][c+1]==1:
                break
            else:
                c+=1
    else:
        d=(d+4-1)%4
        if d==0:
            if graph[r-1][c]==0 and not visited[r-1][c]:
                r-=1
        elif d==1:
            if graph[r][c+1]==0 and not visited[r][c+1]:
                c+=1
        elif d==2:
            if graph[r+1][c]==0 and not visited[r+1][c]:
                r+=1
        else:
            if graph[r][c-1]==0 and not visited[r][c-1]:
                c-=1

print(cnt)