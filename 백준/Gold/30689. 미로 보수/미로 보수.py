import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

maze = [list(input().strip()) for _ in range(n)]
cost = [list(map(int, input().strip().split())) for _ in range(n)]
result = 0
visited = [[False] * m for _ in range(n)]
queue = deque()

dic = {}
dic['U'] = (-1, 0)
dic['D'] = (1, 0)
dic['R'] = (0, 1)
dic['L'] = (0, -1)


def dfs(x, y) :
    global result

    nx = x + dic[maze[x][y]][0]
    ny = y + dic[maze[x][y]][1]

    if 0 <= nx < n and 0 <= ny < m :
        if not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))
            dfs(nx, ny)
            queue.pop()
        else :
            min_cost = float('inf')
            index = len(queue) - 1

            while index >= 0 and (queue[index][0] != nx or queue[index][1] != ny) :
                i, j = queue[index]
                min_cost = min(min_cost, cost[i][j])
                index -= 1

            if index >= 0 and queue[index][0] == nx and queue[index][1] == ny :
                result += min(min_cost, cost[queue[index][0]][queue[index][1]])

for i in range(n) :
    for j in range(m) :
        if not visited[i][j]:
            visited[i][j] = True
            queue.append((i, j))
            dfs(i, j)
            queue.pop()

print(result)