import sys
input = sys.stdin.readline

g = int(input())
ans = []

# 현 몸무게의 최대 값은 50,000
currrent, next = 1, 1
while next <= 50000:
    diff = next**2 - currrent**2
    if diff == g:
        ans.append(next)
        next += 1
        currrent += 1
    elif diff < g:
        next += 1
    else:
        currrent += 1
    
if len(ans) == 0:
    ans.append(-1)
for x in ans:
    print(x)