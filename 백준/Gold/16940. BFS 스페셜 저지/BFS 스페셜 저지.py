import sys
from collections import deque

input = sys.stdin.readline
ans = []


def solve(N, graph, order) :

    visited = [False for _ in range(N+1)]
    queue = deque()

    queue.append(1)
    visited[1] = True

    rank = [-1 for i in range(N+1)]

    for i in range(1,N+1) :
        rank[order[i-1]] = i 
    
    
    for i in range(1,N+1) :
        graph[i] = sorted(graph[i], key=lambda x : rank[x])

    while queue :
        temp = queue.popleft()
        ans.append(temp)

        for element in graph[temp] :
            if visited[element] == False :
                visited[element] = True
                queue.append(element)

    if ans == order :
        print(1)
    else :
        print(0)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(1,N) :
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

order = list(map(int,input().split()))

solve(N,graph,order)