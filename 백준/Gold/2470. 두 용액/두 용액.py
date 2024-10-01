import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = sys.maxsize
left, right = 0, n - 1

arr.sort()
x, y = 0, n - 1

while x < y:
    mix = arr[x] + arr[y]
    if abs(mix) < ans:
        ans = abs(mix)
        left = x
        right = y

    if mix > 0:
        y -= 1
    elif mix < 0:
        x += 1
    else:
        break

print(arr[left], arr[right])