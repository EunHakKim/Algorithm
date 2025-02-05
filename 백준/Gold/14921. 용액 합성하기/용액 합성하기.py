import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = a[-1] + a[0]

start, end = 0, n - 1
while start < end:
    state = a[end] + a[start]
    if state == 0:
        ans = 0
        break
    elif state > 0:
        if abs(state) < abs(ans):
            ans = state
        end -= 1
    else:
        if abs(state) < abs(ans):
            ans = state
        start += 1

print(ans)