import sys
from collections import deque

input = sys.stdin.readline
ans = []


def solve(n, graph, order) :

    visited = [False for _ in range(n+1)]
    queue = deque()

    queue.append(1)
    visited[1] = True
    

    rank = [-1 for i in range(n+1)]

    for i in range(1,n+1) :
        rank[order[i-1]] = i 
    
    
    for i in range(1,n+1) :
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

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(1,n) :
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

order = list(map(int,input().split()))

solve(n,graph,order)