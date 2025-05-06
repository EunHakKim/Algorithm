import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, 0
each = a[0]
ans = 0

while True:
    if each > m:
        if left == right:
            left += 1
            right += 1
            if right >= n:
                break
            each = a[right]
        else:
            each -= a[left]
            left += 1
    elif each < m:
        right += 1
        if right >= n:
            break
        each += a[right]
    else:
        ans += 1
        if left == right:
            left += 1
            right += 1
            if right >= n:
                break
            each = a[right]
        else:
            each -= a[left]
            left += 1

print(ans)