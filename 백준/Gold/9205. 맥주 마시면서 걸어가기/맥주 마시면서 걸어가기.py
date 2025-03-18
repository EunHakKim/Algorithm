import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    home = tuple(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))
    visited = [False] * n
    queue = deque([home])
    happy = False
    while queue:
        x, y = queue.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            happy = True
            break
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))
                    visited[i] = True
    if happy:
        print("happy")
    else:
        print("sad")