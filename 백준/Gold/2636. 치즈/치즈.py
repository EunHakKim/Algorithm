import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cheeze_copy=[]
result=0
cnt=0

def bfs():
    queue = deque()
    visited[0][0]=True
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if cheeze[ny][nx]==0:
                    if not visited[ny][nx]:
                        visited[ny][nx]=True
                        queue.append((nx,ny))
                else:
                    if not visited[ny][nx]:
                        visited[ny][nx]=True
                        cheeze[ny][nx]=0

while True:
    flag=False
    for i in range(n):
        for j in range(m):
            if cheeze[i][j]==1:
                flag = True
    if not flag:
        break
    visited=[[False]*m for _ in range(n)]
    cheeze_copy = copy.deepcopy(cheeze)
    bfs()
    result+=1

for i in range(n):
    for j in range(m):
        if cheeze_copy[i][j]==1:
            cnt+=1

print(result)
print(cnt)