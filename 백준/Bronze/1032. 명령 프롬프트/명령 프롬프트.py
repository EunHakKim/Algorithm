import sys
input = sys.stdin.readline

n = int(input())
files = [list(input().strip()) for _ in range(n)]
ans = ''

for i in range(len(files[0])):
    temp = True
    for j in range(1, n):
        if files[j][i] != files[j - 1][i]:
            temp = False
    if temp:
        ans += files[0][i]
    else:
        ans += '?'

print(ans)