import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m=map(int,input().strip().split())
campus=[list(input().strip()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,-1,0,1]
result=0

def dfs(x,y):
    global result
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<m and 0<=ny<n:
            if not visited[ny][nx] and campus[ny][nx]!="X":
                visited[ny][nx]=True
                if campus[ny][nx]=="P":
                    result+=1
                dfs(nx,ny)

for j in range(n):
    for i in range(m):
        if campus[j][i]=="I":
            dfs(i,j)
if result==0:
    print("TT")
else:
    print(result)