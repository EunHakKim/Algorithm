import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

def solution(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] < arr[x][y]:
                    dp[x][y] += solution(nx, ny)

    return dp[x][y]
    
print(solution(0, 0))