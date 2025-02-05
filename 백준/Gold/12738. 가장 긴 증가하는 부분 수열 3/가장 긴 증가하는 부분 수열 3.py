import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def binary_search(st, en, target):
    while st <= en:
        mid = (st + en) // 2
        if result[mid] == target:
            return mid
        elif result[mid] < target:
            st = mid + 1
        else:
            en = mid - 1

    return st

result = [a[0]]

for i in range(1,len(a)):
    if result[-1] < a[i]:
        result.append(a[i])
    else:
        result[binary_search(0,len(result)-1,a[i])] = a[i]


print(len(result))
