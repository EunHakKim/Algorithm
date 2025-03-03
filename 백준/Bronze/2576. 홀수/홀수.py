import sys
input = sys.stdin.readline

s = 0
m = sys.maxsize

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        s += n
        m = min(m, n)

if s == 0:
    print(-1)
else:
    print(s)
    print(m)