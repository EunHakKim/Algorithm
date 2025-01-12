import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    print(1, 1)
else:
    print(2 * n - 2)
    for i in range(1, n + 1):
        print(1, i)
    for i in range(2, n):
        print(n, i)