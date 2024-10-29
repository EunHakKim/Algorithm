import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
kevin = [0] * (n + 1)
kevin[0] = sys.maxsize

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end):
    visited = [0] * (n + 1)
    visited[start] = 1
    queue = deque([start])
    while queue:
        temp  = queue.popleft()
        if temp == end:
            return visited[temp]
        for x in graph[temp]:
            if not visited[x]:
                queue.append(x)
                visited[x] = visited[temp] + 1

for i in range(1, n):
    for j in range(i + 1, n + 1):
        step = bfs(i, j)
        kevin[i] += step
        kevin[j] += step

print(kevin.index(min(kevin)))