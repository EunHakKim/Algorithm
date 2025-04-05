import sys
input = sys.stdin.readline

n = int(input())
tang = list(map(int, input().split()))
left, right = 0, 0
fruits = [0] * 10
fruits[tang[0]] = 1
ans = 1

while True:
    if fruits.count(0) >= 8:
        ans = max(ans, right - left + 1)
        if right == n - 1:
            break
        right += 1
        fruits[tang[right]] += 1
    else:
        fruits[tang[left]] -= 1
        left += 1

if fruits.count(0) >= 8:
    ans = max(ans, right - left + 1)
print(ans)
