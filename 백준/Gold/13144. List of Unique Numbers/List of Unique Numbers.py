import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0
visited = [False]*100001
left, right = 0, 0
while right < n:
    if not visited[arr[right]]:
        visited[arr[right]] = True
        right += 1
        result += right - left
    else:
        while visited[arr[right]]:
            visited[arr[left]] = False
            left += 1
print(result)