import sys
input = sys.stdin.readline

arr = input().strip()
bomb = input().strip()

stack = []
bomb_len = len(bomb)

for i in range(len(arr)):
    stack.append(arr[i])
    if "".join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")