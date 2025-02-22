import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ways = [i for i in range(101)]
ans = [sys.maxsize for _ in range(101)]

for _ in range(n + m):
    st, en = map(int, input().split())
    ways[st] = en

def bfs(st):
    queue = deque([st])
    ans[st] = 0
    while queue:
        temp = queue.popleft()
        for i in range(1, 7):
            if 0 < temp + i <= 100:
                #ans[temp + i] = min(ans[temp + i], ans[temp] + 1)
                if ans[ways[temp + i]] > ans[temp] + 1:
                    ans[ways[temp + i]] = ans[temp] + 1
                    queue.append(ways[temp + i])

bfs(1)
print(ans[100])