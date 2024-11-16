import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = int(input())
target = 0

while s > 0 and target < n:
    if a[target] == max(a[target:min(target+s+1, n)]):
        target += 1
        continue

    idx = a.index(max(a[target:min(target+s+1, n)]))
    temp = a[idx]
    s -= idx - target
    a.remove(temp)
    a.insert(target, temp)
    target += 1

print(*a)