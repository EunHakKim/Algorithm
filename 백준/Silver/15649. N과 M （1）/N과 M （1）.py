import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

def back(depth):
    if depth == m:
        print(*ans)
        return
    
    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            back(depth + 1)
            ans.pop()

back(0)
