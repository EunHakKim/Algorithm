import sys
input = sys.stdin.readline

x = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
ans = 0

for i in range(7):
    if x >= stick[i]:
        ans += 1
        x -= stick[i]

    if x == 0:
        break

print(ans)