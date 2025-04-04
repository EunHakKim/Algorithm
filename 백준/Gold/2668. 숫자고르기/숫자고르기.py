import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
visited = [False] * n
ans = set([])

def dfs(first, index, second):
    if first == index - 1:
        for x in second:
            ans.add(x)
    
    if not visited[index - 1]:
        visited[index - 1] = True
        second.append(nums[index - 1])
        dfs(first, nums[index - 1], second)
    

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, nums[i], [nums[i]])

ans = list(ans)
ans.sort()
print(len(ans))
for x in ans:
    print(x)