import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
people = list(map(int, input().split()))
animals = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0

people.sort()
    
for x, y in animals:
    if y > l:
        continue

    st, en = 0, m - 1
    min = x + y - l
    max = x - y + l
    
    while st <= en:
        mid = (st + en) // 2
        if min <= people[mid] <= max:
            cnt += 1
            break
        elif people[mid] < max:
            st = mid + 1
        else:
            en = mid - 1

print(cnt)