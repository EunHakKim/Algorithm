import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

target_list = [list(map(int, input().split())) for _ in range(m)]

def bfs(st, en):
    queue = deque([st])
    visited = [-1] * (n + 1)
    visited[st] = 0
    while queue:
        temp = queue.popleft()
        if temp == en:
            return visited[temp]
        for a, b in graph[temp]:
            if visited[a] == -1:
                visited[a] = visited[temp] + b
                queue.append(a)

for target in target_list:
    print(bfs(target[0], target[1]))