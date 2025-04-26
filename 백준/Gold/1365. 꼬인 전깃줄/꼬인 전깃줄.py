import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def binary_search(arr, target):
    st, en = 0, len(arr) - 1
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return st

lis = [nums[0]]
for i in range(1, n):
    if nums[i] > lis[-1]:
        lis.append(nums[i])
    else:
        index = binary_search(lis, nums[i])
        lis[index] = nums[i]

print(n - len(lis))