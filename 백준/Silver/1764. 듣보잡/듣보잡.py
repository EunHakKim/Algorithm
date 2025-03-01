import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = []
ans = []

for _ in range(n):
    name = input().strip()
    arr1.append(name)
arr1.sort()

def find(name):
    st, en = 0, n - 1
    while st < en:
        mid = (st + en) // 2
        if arr1[mid] < name:
            st = mid + 1
        else:
            en = mid
    if arr1[st] == name or arr1[en] == name:
        return True
    else:
        return False

for _ in range(m):
    name = input().strip()
    if find(name):
        ans.append(name)

ans.sort()
print(len(ans))
for name in ans:
    print(name)
    