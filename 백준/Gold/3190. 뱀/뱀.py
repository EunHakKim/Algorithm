import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
apple = []
for _ in range(k):
    x, y = map(int,input().split())
    apple.append((y-1,x-1))
l = int(input())
direction = deque([])
for _ in range(l):
    x, c = input().strip().split()
    direction.append((int(x), c))
snake = deque([(0,0)])
s_direction = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt=0

while True:
    cnt+=1
    x, y = snake[-1]
    nx = x + dx[s_direction]
    ny = y + dy[s_direction]
    if (nx, ny) in snake:
        break
    elif not (0<=nx<n and 0<=ny<n):
        break

    if (nx, ny) in apple:
        snake.append((nx,ny))
        apple.remove((nx, ny))
    else:
        snake.append((nx, ny))
        snake.popleft()
    
    if len(direction)>0:
        s,c=direction[0]
        if s==cnt:
            direction.popleft()
            if c=="D":
                s_direction = (s_direction+1)%4
            else:
                s_direction = (s_direction-1)%4

print(cnt)