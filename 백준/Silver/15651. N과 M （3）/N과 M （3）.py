import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

def back(ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        ans.append(i)
        back(ans)
        ans.pop()

back(ans)