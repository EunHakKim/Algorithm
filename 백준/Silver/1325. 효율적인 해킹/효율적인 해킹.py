import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
max_com = 1
result=[]
for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

def bfs(index):
    chk=[0]*(n+1)
    each=1
    queue=deque([index])
    chk[index]=1
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not chk[i]:
                chk[i]=1
                each+=1
                queue.append(i)
    return each

for i in range(1,n+1):
    each = bfs(i)
    if each > max_com:
        max_com = each
        result=[i]
    elif each == max_com:
        result.append(i)

print(*result)