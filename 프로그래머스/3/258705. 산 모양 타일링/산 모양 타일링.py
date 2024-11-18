def solution(n, tops):
    answer = 0
    dp = [1, 1]
    for i in range(2, 2 * n + 2):
        if i % 2 == 0:
            if tops[i // 2 - 1] == 1:
                dp.append((dp[i - 1] * 2 + dp[i - 2]) % 10007)
            else:
                dp.append((dp[i - 1] + dp[i - 2]) % 10007)
        else:
            dp.append((dp[i - 1] + dp[i - 2]) % 10007)
    return dp[2 * n + 1]