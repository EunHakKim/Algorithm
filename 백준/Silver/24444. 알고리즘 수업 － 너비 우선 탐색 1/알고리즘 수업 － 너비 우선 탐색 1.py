import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for edge in edges:
    edge.sort()

visited[r], i = 1, 1
queue = deque([r])
#bfs
while queue:
    node = queue.popleft()
    for next in edges[node]:
        if visited[next] == 0:
            i += 1
            visited[next] = i
            queue.append(next)

for i in range(1, n + 1):
    print(visited[i])