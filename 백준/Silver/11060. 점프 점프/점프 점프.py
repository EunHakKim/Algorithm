import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
miro = list(map(int, input().split()))
visited = [-1] * n
visited[0] = 0

queue = deque([0])
while queue:
    temp = queue.popleft()
    if miro[temp] == 0:
        continue

    for i in range(1, miro[temp] + 1):
        if temp + i < n:
            if visited[temp + i] == -1:
                visited[temp + i] = visited[temp] + 1
                queue.append(temp + i)

print(visited[n - 1])
