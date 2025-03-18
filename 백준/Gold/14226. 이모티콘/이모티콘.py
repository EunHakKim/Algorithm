import sys
from collections import deque
input = sys.stdin.readline

target = int(input())
visited = [[-1] * 2000 for _ in range(2000)]
queue = deque([(1, 0)])
visited[1][0] = 0
while queue:
    s, c = queue.popleft()
    if target == s:
        print(visited[s][c])
        break
    #1
    if visited[s][s] == -1:
       visited[s][s] = visited[s][c] + 1
       queue.append((s, s))
    #2
    if s + c < 2000 and visited[s + c][c] == -1:
        visited[s + c][c] = visited[s][c] + 1
        queue.append((s + c, c))
    #3
    if s - 1 >= 0 and visited[s - 1][c] == -1:
        visited[s - 1][c] = visited[s][c] + 1
        queue.append((s - 1, c))