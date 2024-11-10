def solution(n, m, x, y, r, c, k):
    answer = ''
    if k < abs(r - x) + abs(c - y):
        return 'impossible'
    if (k - abs(r - x) + abs(c - y)) % 2 == 1:
        return 'impossible'
    
    while k - (abs(r - x) + abs(c - y)) > 0 and x < n:
        answer += 'd'
        x += 1
        k -= 1
        
    while k - (abs(r - x) + abs(c - y)) > 0 and y > 1:
        answer += 'l'
        y -= 1
        k -= 1
    
    remain = k - (abs(r - x) + abs(c - y))
    for i in range(remain//2):
        answer += 'rl'
        k -= 2
    
    row = abs(x - r)
    col = abs(y - c)
    if x < r:
        answer += 'd' * row

    if y > c:
        answer += 'l' * col

    if y < c:
        answer += 'r' * col

    if x > r:
        answer += 'u' * row
    
    return answer