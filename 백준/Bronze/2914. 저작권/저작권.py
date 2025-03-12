import sys
input = sys.stdin.readline

a, i = map(int, input().split())
ans = a * i
while True:
    if ((ans - 1) / a) <= (i - 1):
        break
    ans -= 1
print(ans)