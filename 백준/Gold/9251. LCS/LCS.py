import sys
input = sys.stdin.readline

arr1 = "-" + input().strip()
arr2 = "-" + input().strip()

dp = [[0] * (len(arr2)) for _ in range(len(arr1))]

for i in range(1, len(arr1)):
    for j in range(1, len(arr2)):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[-1][-1])