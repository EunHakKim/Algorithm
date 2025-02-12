import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # mCn
    c, d = 1, 1
    for i in range(n + 1, m + 1):
        c *= i
    for i in range(1, m - n + 1):
        d *= i
    print(c // d)