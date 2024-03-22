from collections import deque

N, M=map(int,input().split())
visited=[False] * (N+1)
visited[0]=True
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

connected=0

def bfs(index):
    queue=deque([index])
    visited[index]=True
    while queue:
        temp=queue.popleft()
        for i in range(1,N+1):
            if not visited[i] and graph[temp][i]:
                queue.append(i)
                visited[i]=True


while True:
    if False not in visited:
        break
    temp=visited.index(False)
    bfs(temp)
    connected+=1

print(connected)