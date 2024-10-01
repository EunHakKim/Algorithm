import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = sys.maxsize
left = 0
right = len(arr) - 1

arr.sort()
x, y = 0, len(arr) - 1

while True:
    mix = arr[x] + arr[y]
    if abs(mix) < ans:
        ans = abs(mix)
        left = x
        right = y

    if mix > 0:
        y -= 1
        if x == y:
            y -= 1
        if y < 0:
            break
    elif mix < 0:
        x += 1
        if x == y:
            x += 1
        if x > len(arr) - 1:
            break
    else:
        break

if arr[left] < arr[right]:
    print(arr[left], arr[right])
else:
    print(arr[right], arr[left])