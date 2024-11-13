import sys
input = sys.stdin.readline

n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n

dp[0] = works[0][0]

while 0 in dp:
    for i in range(n):
        if dp[i] == 0:
            max_time = 0
            temp = False
            for j in range(works[i][1]):
                if dp[works[i][2 + j]-1] == 0:
                    temp = True
                    break
                else:
                    max_time = max(max_time, dp[works[i][2 + j]-1])
            if not temp:
                dp[i] = max_time + works[i][0]

print(max(dp))
