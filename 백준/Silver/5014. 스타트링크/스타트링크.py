import sys
from collections import deque
input = sys.stdin.readline

f,s,g,u,d = map(int, input().split())
chk = [-1]*(f+1)

def bfs(f,s,g,u,d):
    queue = deque([s])
    chk[s]=0
    while queue:
        temp = queue.popleft()
        if temp == g:
            print(chk[temp])
            exit()
        if 1 <= temp + u <= f:
            if chk[temp + u] == -1:
                chk[temp + u] = chk[temp] + 1
                queue.append(temp + u)
        if 1 <= temp - d <= f:
            if chk[temp - d] == -1:
                chk[temp - d] = chk[temp] + 1
                queue.append(temp - d)

bfs(f,s,g,u,d)
print("use the stairs")