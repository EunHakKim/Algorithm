def solution(coin, cards):
    # -1: 등장 전, 0: 등장 후 & 구매 전, 1: 구매 후 & 사용 전, 2: 사용 후
    n = len(cards)
    visited = [-1] * (n + 1)
    can_use = 0
    staging = 0
    ans = 1
    for i in range(n // 3):
        visited[cards[i]] = 1
        if visited[n + 1 - cards[i]] == 1:
            can_use += 1
    
    for i in range(n // 3, n, 2):
        for j in range(2):
            visited[cards[i + j]] = 0
            if coin > 0:
                if visited[n + 1 - cards[i + j]] == 1:
                    coin -= 1
                    can_use += 1
                elif visited[n + 1 - cards[i + j]] == 0:
                    staging += 1
        
        if can_use > 0:
            can_use -= 1
        elif coin > 1 and staging > 0:
            coin -= 2
            staging -= 1
        else:
            return ans
        ans += 1
    return ans