import math

def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    ans = dict(zip(enroll, [0 for _ in range(len(enroll))]))
    
    for i in range(len(seller)):
        money = amount[i] * 100
        now = seller[i]
    
        while True:
            if money < 10:
                ans[now] += money
                break
            else:
                ans[now] += math.ceil(money * 0.9)
                if parent[now] == "-":
                    break
                money = math.floor(money * 0.1)
                now = parent[now]

    return list(ans.values())