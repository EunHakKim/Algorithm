import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
nums = [0] + list(map(int, input().split())) + [l]
nums.sort()

st, en = 1, l - 1
ans = 0
while st <= en:
    cnt = 0
    mid = (st + en) // 2
    for i in range(1, n + 2):
        if nums[i] - nums[i - 1] > mid:
            cnt += (nums[i] - nums[i - 1] - 1) // mid
    if cnt > m:
        st = mid + 1
    else:
        en = mid - 1
        ans = mid

print(ans)