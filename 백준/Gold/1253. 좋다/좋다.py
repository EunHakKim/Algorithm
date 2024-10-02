import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = 0

a.sort()
left, right = 0, n-1
sum = a[0] + a[n-1]

for i in range(n):
    if i == 0:
        left, right = 1, n-1
    elif i == n-1:
        left, right = 0, n-2
    else:
        left, right = 0, n-1

    while left < right:
        sum = a[left] + a[right]
        if a[i] < sum:
            right -= 1
            if right == i:
                right -= 1
        elif a[i] > sum:
            left += 1
            if left == i:
                left += 1
        else:
            ans += 1
            break

if n == 1:
    print(0)
else:
    print(ans)