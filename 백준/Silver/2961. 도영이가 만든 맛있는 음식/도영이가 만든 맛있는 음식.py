import sys
input = sys.stdin.readline

n = int(input())
foods = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = sys.maxsize

def back(sour, bitter, depth):
    global ans
    if depth != 0:
        ans = min(ans, abs(sour - bitter))
    if depth == 10:
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            back(sour * foods[i][0], bitter + foods[i][1], depth + 1)
            visited[i] = False

back(1, 0, 0)

print(ans)