import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x=map(int,input().strip().split())
arr = [[] for _ in range(n+1)]
cnt=[-1]*(n+1)

for _ in range(m):
    a, b= map(int,input().strip().split())
    arr[a].append(b)

def bfs(index):
    queue = deque()
    queue.append(index)
    cnt[index]=0
    while queue:
        temp = queue.popleft()
        for i in arr[temp]:
            if cnt[i]==-1:
                cnt[i]=cnt[temp]+1
                queue.append(i)

bfs(x)
if k not in cnt:
    print(-1)
else:
    for i in range(n+1):
        if cnt[i]==k:
            print(i)