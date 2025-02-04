import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
left, right = 0, 1
diff = a[-1] - a[0]

while right < n:
    if m > a[right]-a[left]:
        right += 1
    elif m < a[right]-a[left]:
        if left + 1 >= right:
            diff = min(diff, a[right]-a[left])
            left += 1
            right += 1 
        else:
            diff = min(diff, a[right]-a[left])
            left += 1
    else:
        diff = m
        break

print(diff)