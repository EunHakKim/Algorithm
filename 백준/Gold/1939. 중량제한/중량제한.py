import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
max_weight = 0
bridge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    max_weight = max(max_weight, c)
    bridge[a].append((b, c))
    bridge[b].append((a, c))
start, end = map(int, input().split())

def bfs(mid):
    global start, end
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    while queue:
        temp = queue.popleft()
        if temp == end:
            return True
        for a, b in bridge[temp]:
            if not visited[a] and mid <= b:
                queue.append(a)
                visited[a] = True
    return False

def search(st, en):
    if st >= en:
        if bfs(st):
            print(st)
        else:
            print(st - 1)
        return

    mid = (st + en) // 2
    check = bfs(mid)
    if check:
        search(mid + 1, en)
    else:
        search(st, mid)

search(0, max_weight)