import sys
from collections import deque
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
visited = [[[-1] * 61 for _ in range(61)] for __ in range(61)]

if n == 1:
    scv.append(0)
if n <= 2:
    scv.append(0)

visited[scv[0]][scv[1]][scv[2]] = 0
queue = deque([(scv[0], scv[1], scv[2])])
while queue:
    s1, s2, s3 = queue.popleft()
    if s1 == 0 and s2 == 0 and s3 == 0:
        break

    for a, b, c in permutations([9, 3, 1], 3):
        scv1, scv2, scv3 = s1 - a, s2 - b, s3 - c
        scv1, scv2, scv3 = max(0, scv1), max(0, scv2), max(0, scv3)
        if visited[scv1][scv2][scv3] == -1:
            visited[scv1][scv2][scv3] = visited[s1][s2][s3] + 1
            queue.append((scv1, scv2, scv3))

print(visited[0][0][0])