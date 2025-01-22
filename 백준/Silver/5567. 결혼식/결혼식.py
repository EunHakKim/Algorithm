import sys
from collections import Counter, deque
input = sys.stdin.readline

n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs():
    queue = deque([1])
    visited[1] = 0
    while queue:
        v = queue.popleft()
        if visited[v] >= 2:
            return
        for i in friends[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs()
counter = Counter(visited)
print(counter[1] + counter[2])