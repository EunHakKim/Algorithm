import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    apply = [list(map(int, input().split())) for _ in range(n)]
    apply.sort()
    top = apply[0][1]
    ans = 1

    for i in range(1, n):
        if apply[i][1] < top:
            top = apply[i][1]
            ans += 1
    print(ans)
    