from collections import deque
import sys
sys.setrecursionlimit(200000)

N, K=map(int,input().split())
depth=[-1]*200000
graph=[[] for _ in range(200000)]
result=[]

def bfs(N, K):
    queue=deque([N])
    depth[N]=0
    while queue:
        temp=queue.popleft()
        if temp==K:
            print(depth[temp])
            result.append(N)
            dfs(N, K)
            exit()
        for i in [temp-1, temp+1, 2*temp]:
            if 0<=i<200000:
                if depth[i]==-1:
                    depth[i]=depth[temp]+1
                    graph[temp].append(i)
                    queue.append(i)

def dfs(N, K):
    if N==K:
        print(*result)
        exit()

    for i in graph[N]:
        result.append(i)
        dfs(i,K)
        result.pop()


bfs(N, K)