import sys
input = sys.stdin.readline

n = int(input())
ans = ''

def back(ans, depth):
    for i in range(1, depth // 2 + 1):
        if ans[depth - i:] == ans[depth - 2 * i : depth - i]:
            return
    
    if depth == n:
        print(int(ans))
        exit()
    
    for i in range(1, 4):
        back(ans + str(i), depth + 1)

back(ans, 0)