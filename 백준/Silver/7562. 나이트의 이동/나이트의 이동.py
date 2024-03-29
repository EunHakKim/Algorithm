import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
for _ in range(N):
    L=int(input())
    current=list(map(int,input().split()))
    target=list(map(int,input().split()))

    queue=deque([(current[0],current[1])])
    chess=[[-1]*L for __ in range(L)]
    chess[current[1]][current[0]]=0

    dx=[1,2,2,1,-1,-2,-2,-1]
    dy=[2,1,-1,-2,-2,-1,1,2]

    while queue:
        x, y=queue.popleft()
        
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<L and 0<=ny<L:
                if chess[ny][nx]==-1:
                    chess[ny][nx]=chess[y][x]+1
                    queue.append((nx,ny))

        if chess[target[1]][target[0]]!=-1:
            print(chess[target[1]][target[0]])
            break