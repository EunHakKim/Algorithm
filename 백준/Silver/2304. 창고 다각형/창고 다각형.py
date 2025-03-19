import sys
input = sys.stdin.readline

n = int(input())
point, top = [], 0
h = []
for _ in range(n):
    x, y = map(int, input().split())
    if y > top:
        point.clear()
        point.append(x)
        top = y
    elif y == top:
        point.append(x)
    h.append((x, y))

h.sort()
point.sort()
x, y = h[0]
ans = (point[-1] - point[0] + 1) * top
for i in range(1, n):
    cx, cy = h[i]
    if cx <= point[0]:
        if cy > y:
            ans += abs(cx - x) * y
            x, y = cx, cy
    else:
        break
x, y = h[n - 1]
for i in range(n - 2, -1, -1):
    cx, cy = h[i]
    if cx >= point[-1]:
        if cy > y:
            ans += abs(cx - x) * y
            x, y = cx, cy
    else:
        break

print(ans)

#시작 -> point[0] 올라가야 함
#point[-1] -> 끝 내려가야 함