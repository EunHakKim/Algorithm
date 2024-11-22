from itertools import combinations, product

def solution(dice):
    answer = []
    temp_score = 0
    divides = combinations(range(len(dice)), len(dice) // 2)
    
    for divide in divides:
        a_sum = [0]
        b_sum = [0] 
        
        for i in range(len(dice)):
            if i in divide:
                a_sum = [sum(comb) for comb in product(dice[i], a_sum)]
            else:
                b_sum = [sum(comb) for comb in product(dice[i], b_sum)]
        
        a_sum.sort()
        b_sum.sort()
        score = 0
        a = 0
        b = 0
        
        while a < len(a_sum) and b < len(b_sum):
            if a_sum[a] > b_sum[b]:
                score += len(a_sum) - a
                b += 1
            else:
                a += 1
        
        if score > temp_score:
            temp_score = score
            answer = [s + 1 for s in divide]
    
    return answer