import sys
input = sys.stdin.readline

n, k = map(int, input().split())
train = [list(map(int, input().split())) for _ in range(n)]
# 티켓을 검사한 손님, 티켓을 검사하지 않은 손님
check_max = [[0, 0] for _ in range(n + 1)]
check_min = [[0, 0] for _ in range(n + 1)]
ans_max = 0
ans_min = 0

for i in range(n):
    a, b = train[i][0], train[i][1]
    #하차 처리(최대)
    if check_max[i][1] >= a:
        check_max[i][1] -= a
        ans_max += a
    else:
        ans_max += check_max[i][1]
        check_max[i][0] -= a - check_max[i][1]
        check_max[i][1] = 0

    #하차 처리(최소)
    if check_min[i][0] >= a:
        check_min[i][0] -= a
    else:
        ans_min += a - check_min[i][0]
        check_min[i][1] -= a - check_min[i][0]
        check_min[i][0] = 0
        
    #승차 처리
    check_max[i + 1][1] = check_max[i][1] + b
    check_max[i + 1][0] = check_max[i][0]

    check_min[i + 1][1] = check_min[i][1] + b
    check_min[i + 1][0] = check_min[i][0]

    #티켓 검사
    if i % k == 0:
        check_max[i + 1][0] += check_max[i + 1][1]
        check_max[i + 1][1] = 0

        check_min[i + 1][0] += check_min[i + 1][1]
        check_min[i + 1][1] = 0
    
print(ans_min, ans_max)