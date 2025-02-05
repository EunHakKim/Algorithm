import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

start = min(T)
end = max(T) * M
ans = end

while start <= end:
    result = 0
    mid = (start + end) // 2

    for i in range(N):
        result += mid // T[i]

    if result >= M:
        end = mid - 1
        ans = min(mid, ans)
    else:
        start = mid + 1
print(ans)