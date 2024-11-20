import sys
input = sys.stdin.readline

n = int(input())
scales = list(map(int, input().split()))
scales.sort()

ans = 1

for scale in scales:
    if ans < scale:
        break
    ans += scale

print(ans)