import sys
from collections import deque
sys.setrecursionlimit(10**9)


def dfs(x, cnt):
    if check[x]:
        if cnt - result[x] >= 3:
            return x
        else: 
            return -1
    check[x] = 1
    result[x] = cnt
    for y in graph[x]:
        startNode = dfs(y, cnt + 1)
        if startNode != -1:
            check[x] = 2
            if x == startNode: 
                return -1
            else: 
                return startNode
    return -1

N = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]
check = [0] * (N + 1)
result = [0] * (N + 1)

for _ in range(N):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1, 0)
q = deque()
for i in range(1, N + 1):
    if check[i] == 2:
        q.append(i)
        result[i] = 0
    else:
        result[i] = -1
while q:
    x = q.popleft()
    for y in graph[x]:
        if result[y] == -1:
            q.append(y)
            result[y] = result[x] + 1
print(*result[1:])