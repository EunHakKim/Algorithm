from collections import deque

N, K=map(int,input().split())
depth=[-1]*200000

def bfs(N, K):
    queue=deque([N])
    depth[N]=0
    while queue:
        temp=queue.popleft()
        if temp==K:
            print(depth[temp])
            exit()
        for i in [temp-1, temp+1, 2*temp]:
            if 0<=i<200000:
                if depth[i]==-1:
                    depth[i]=depth[temp]+1
                    queue.append(i)

bfs(N, K)