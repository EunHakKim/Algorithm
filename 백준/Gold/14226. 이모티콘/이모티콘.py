import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
visited = [[-1] * 1001 for _ in range(1001)]
visited[1][0] = 0
queue = deque([(1, 0)])
while queue:
    b, c = queue.popleft()
    if b == s:
        print(visited[b][c])
        exit()

    # 1
    if visited[b][b] == -1:
        visited[b][b] = visited[b][c] + 1
        queue.append((b, b))

    # 2
    if b + c < 1001:
        if visited[b + c][c] == -1:
            visited[b + c][c] = visited[b][c] + 1
            queue.append((b + c, c))

    # 3
    if b - 1 >= 0:
        if visited[b - 1][c] == -1:
            visited[b - 1][c] = visited[b][c] + 1
            queue.append((b - 1, c))