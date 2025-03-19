import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

n, m, x, y, k = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dicer = deque([0, 0, 0, 0])
dicec = deque([0, 0, 0, 0])

def rotation(i):
    if i == 1:
        dicer.appendleft(dicer.pop())
        dicec[1], dicec[3] = dicer[1], dicer[3]
    elif i == 2:
        dicer.append(dicer.popleft())
        dicec[1], dicec[3] = dicer[1], dicer[3]
    elif i == 3:
        dicec.append(dicec.popleft())
        dicer[1], dicer[3] = dicec[1], dicec[3]
    else:
        dicec.appendleft(dicec.pop())
        dicer[1], dicer[3] = dicec[1], dicec[3]


for i in range(len(commands)):
    nx, ny = x + dx[commands[i] - 1], y + dy[commands[i] - 1]
    if not(0 <= nx < n and 0 <= ny <m):
        continue

    rotation(commands[i])
    x, y = nx, ny
    if nums[x][y] == 0:
        nums[x][y] = dicer[3]
    else:
        dicec[3], dicer[3] = nums[x][y], nums[x][y]
        nums[x][y] = 0
    
    print(dicer[1])


