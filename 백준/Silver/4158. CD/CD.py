import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    sang = set([])
    ans = 0

    for _ in range(n):
        sang.add(int(input()))

    for _ in range(m):
        temp = int(input())
        if temp in sang:
            ans += 1

    print(ans)