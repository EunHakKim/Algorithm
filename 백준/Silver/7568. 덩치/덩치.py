n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ans = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            ans[j] += 1
        elif arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            ans[i] += 1

print(*ans)