def solution(mats, park):
    answer = -1
    dp = [[] for _ in range(len(park))]
    for i in range(len(park)):
        for x in park[i]:
            if x == '-1':
                dp[i].append(1)
            else:
                dp[i].append(0)
    
    max_length = 0
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_length = max(max_length, dp[i][j])
    
    for x in mats:
        if x <= max_length and x > answer:
            answer = x
            
    return answer