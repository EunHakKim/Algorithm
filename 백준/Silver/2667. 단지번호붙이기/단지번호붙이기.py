from collections import deque

def dfs(i, j, index, N):
    sums[index]+=1
    visited[i][j]=True
    if i+1<N and visited[i+1][j]==False and map[i+1][j]==1:
        dfs(i+1,j,index,N)
    if j+1<N and visited[i][j+1]==False and map[i][j+1]==1:
        dfs(i,j+1,index,N)
    if i-1>-1 and visited[i-1][j]==False and map[i-1][j]==1:
        dfs(i-1,j,index,N)
    if j-1>-1 and visited[i][j-1]==False and map[i][j-1]==1:
        dfs(i,j-1,index,N)

N=int(input())
map=[list(map(int,input())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
sums=[]
for i in range(N):
    for j in range(N):
        if visited[i][j]==False and map[i][j]==1:
            sums.append(0)
            temp=len(sums)-1
            dfs(i,j,temp,N)
        else:
            visited[i][j]=True

sums.sort()
print(len(sums))
for x in sums:
    print(x)