import sys
from collections import deque
input = sys.stdin.readline

N=int(input().strip())
dist = [[] for _ in range(N+1)]
visited = [False]*(N+1) 

for _ in range(1, N+1):
    connect = list(map(int, input().strip().split()))
    for i in range(1, len(connect)//2):
        dist[connect[0]].append((connect[i*2 - 1], connect[i*2]))
        
result=0
temp=-1

def dfs(index, length):
    global result
    global temp
    if length>result:
        result=length
        temp=index

    for v,d in dist[index]:
        if visited[v]==False:
            visited[v]=True
            dfs(v,length+d)
            visited[v]=False

visited[1]=True
dfs(1,0)
visited[1]=False
visited[temp]=True
dfs(temp,0)
visited[temp]=False

print(result)