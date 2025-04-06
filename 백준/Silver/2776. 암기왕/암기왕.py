import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))

    nums.sort()
    for target in targets:
        st, en = 0, n - 1
        while st < en:
            mid = (st + en) // 2
            if target > nums[mid]:
                st = mid + 1
            else:
                en = mid
        if target == nums[st]:
            print(1)
        else:
            print(0)
