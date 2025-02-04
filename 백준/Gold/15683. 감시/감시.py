import sys
from itertools import product
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
ans = sys.maxsize

for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 4:
            cctvs.append([j, i, graph[i][j]])
        elif graph[i][j] == 5:
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                while True:
                    if not (0 <= nx < m and 0 <= ny < n):
                        break
                    if graph[ny][nx] == 6:
                        break
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = -1
                    nx += dx[k]
                    ny += dy[k]

def check(state):
    global ans
    chk = [arr[:] for arr in graph]
    result = 0
    for i in range(len(cctvs)):
        if cctvs[i][2] == 1 or cctvs[i][2] == 2:
            for k in range(cctvs[i][2]):
                nx = cctvs[i][0] + dx[(state[i] + k * 2) % 4]
                ny = cctvs[i][1] + dy[(state[i] + k * 2) % 4]
                while True:
                    if not (0 <= nx < m and 0 <= ny < n):
                        break
                    if chk[ny][nx] == 6:
                        break
                    if chk[ny][nx] == 0:
                        chk[ny][nx] = -1
                    nx += dx[(state[i] + k * 2) % 4]
                    ny += dy[(state[i] + k * 2) % 4]
        elif cctvs[i][2] == 3 or cctvs[i][2] == 4:
            for k in range(cctvs[i][2] - 1):
                nx = cctvs[i][0] + dx[(state[i] + k) % 4]
                ny = cctvs[i][1] + dy[(state[i] + k) % 4]
                while True:
                    if not (0 <= nx < m and 0 <= ny < n):
                        break
                    if chk[ny][nx] == 6:
                        break
                    if chk[ny][nx] == 0:
                        chk[ny][nx] = -1
                    nx += dx[(state[i] + k)%4]
                    ny += dy[(state[i] + k)%4]
    for arr in chk:
        for x in arr:
            if x == 0:
                result += 1
    #if result < ans:
    
    ans = min(ans, result)

for state in product(range(4), repeat=len(cctvs)):
    check(state)
print(ans)