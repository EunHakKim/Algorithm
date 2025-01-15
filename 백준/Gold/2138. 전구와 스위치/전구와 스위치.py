import sys
input = sys.stdin.readline

n = int(input())
begin = list(input().strip())
begin = [int(x) for x in begin]
target = list(input().strip())
target = [int(x) for x in target]
ans = []

def check(begin, target, first):
    if first:
        switch = 1
        begin[0] = 1 if begin[0] == 0 else 0
        begin[1] = 1 if begin[1] == 0 else 0
    else: 
        switch = 0
    
    for i in range(1, n - 1):
        if begin[i - 1] != target[i - 1]:
            switch += 1
            begin[i - 1] = 1 if begin[i - 1] == 0 else 0
            begin[i] = 1 if begin[i] == 0 else 0
            begin[i + 1] = 1 if begin[i + 1] == 0 else 0
    
    if begin[n - 2] == target[n - 2] and begin[n - 1] == target[n - 1]:
        ans.append(switch)
    elif begin[n - 2] != target[n - 2] and begin[n - 1] != target[n - 1]:
        ans.append(switch + 1)

# 첫번째를 누른 경우
check(begin[:], target[:], True)
# 첫번째를 누르지 않은 경우
check(begin[:], target[:], False)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))