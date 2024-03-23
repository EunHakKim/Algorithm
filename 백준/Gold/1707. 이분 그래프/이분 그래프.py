import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, group):
    queue = deque([start])
    visited[start] = group  
    while queue:  

        x = queue.popleft()  

        for i in graph[x]:  
            if not visited[i]: 
                queue.append(i)  
                visited[i] = -1 * visited[x]  
            elif visited[i] == visited[x]:  
                return False  
    return True


K=int(input())

for _ in range(K):
    V, E=map(int,input().split())
    graph=[[] for ___ in range(V+1)]
    for __ in range(E):
        u, v= map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited=[False]*(V+1)

    for i in range(1, V + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
    