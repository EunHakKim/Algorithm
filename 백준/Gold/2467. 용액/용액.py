import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
left, lans, right, rans = 0, 0, n-1, n-1
add = arr[0] + arr[-1]
ans = abs(add)


while left < right:
    add = arr[left] + arr[right]
    if abs(add) < ans:
        ans = abs(add)
        lans, rans = left, right

    if add > 0:
        right -= 1
    elif add < 0:
        left += 1
    else:
        break

print(arr[lans], arr[rans])