import sys
input = sys.stdin.readline

chess = [list(input().strip()) for _ in range(8)]
ans = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                if chess[i][j] == 'F':
                    ans += 1
        else:
            if j % 2 != 0:
                if chess[i][j] == 'F':
                    ans += 1
        
print(ans)