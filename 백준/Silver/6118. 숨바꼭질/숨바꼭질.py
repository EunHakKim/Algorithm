import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
ans, cnt = 1, 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 0
queue = deque([1])
while queue:
    cx = queue.popleft()
    for nx in graph[cx]:
        if visited[nx] == -1:
            visited[nx] = visited[cx] + 1
            queue.append(nx)

for i in range(1, n + 1):
    if visited[i] > visited[ans]:
        ans = i
        cnt = 1
    elif visited[i] == visited[ans]:
        cnt += 1

print(ans, visited[ans], cnt)