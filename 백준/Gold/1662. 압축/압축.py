import sys
input = sys.stdin.readline

arr = input().strip()
temp = ''
stack = []
ans = 0

for x in arr:
    if x == '(':
        stack.append([ans - 1, temp])
        ans = 0
    elif x == ')':
        target = stack.pop()
        ans = ans * target[1] + target[0]
    else:
        ans += 1
        temp = int(x)

print(ans)  

#71(1()66(5))
#2(1())