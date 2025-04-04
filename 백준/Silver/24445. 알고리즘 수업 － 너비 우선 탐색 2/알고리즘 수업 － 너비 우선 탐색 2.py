import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[r], order = 1, 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort(reverse = True)

queue = deque([r])
while queue:
    cv = queue.popleft()
    for nv in graph[cv]:
        if visited[nv] == 0:
            order += 1
            visited[nv] = order
            queue.append(nv)

for i in range(1, n + 1):
    print(visited[i])