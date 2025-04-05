import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

# 1이 3개미만이면 -1 출력
if dolls.count(1) < k:
    print(-1)
    exit()

lion_cnt, left = 1, 0
while dolls[left] != 1:
    left += 1

right = left
while lion_cnt < k:
    right += 1
    if dolls[right] == 1:
        lion_cnt += 1

ans = right - left + 1
while True:
    right += 1
    if right == n:
        break
    if dolls[right] == 1:
        left += 1
        while dolls[left] != 1:
            left += 1
    ans = min(ans, right - left + 1)

print(ans)
