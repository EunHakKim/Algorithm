import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    #작은 수
    dp = [0,0,1,7,4,2,6,8,10]
    for i in range(9, n + 1):
        little = min(
            int(str(dp[i - 6]) + '0'),
            int(str(dp[i - 2]) + '1'),
            int(str(dp[i - 5]) + '2'),
            int(str(dp[i - 4]) + '3'),
            int(str(dp[i - 3]) + '7'),
            int(str(dp[i - 7]) + '8')
        )
        dp.append(little)
    print(dp[n], end=" ")

    #큰 수
    big = ''
    if n % 2 == 1:
        big += '7'
        n -= 3

    for _ in range(n // 2):
        big += '1'
    print(big)