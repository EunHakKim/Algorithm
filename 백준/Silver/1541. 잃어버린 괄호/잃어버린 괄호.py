import sys
input = sys.stdin.readline

arr = list(input().strip())
ans = 0
num = ''
is_minus = False

for x in arr:
    if x == '-' or x == '+':
        if is_minus:
            ans -= int(num)
            num = ''
        else:
            ans += int(num)
            num = ''
        if x == '-':
            is_minus = True
    else:
        num += x

if is_minus:
    ans -= int(num)
else:
    ans += int(num)

print(ans)