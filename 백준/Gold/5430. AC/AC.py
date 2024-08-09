import sys
from collections import deque
input = sys.stdin.readline

t=int(input())

for _ in range(t):
    p = list(input().strip())
    n = int(input())
    input_str = input().strip()
    if input_str=="[]":
        x = deque([])
    else:
        x = deque(list(map(int, input_str.strip("[]").split(","))))
    temp = False
    reverse = False
    for y in p:
        if y=="R":
            reverse = not reverse
        if y=="D":
            if len(x)!=0:
                if reverse:
                    x.pop()
                else:
                    x.popleft()
            else:
                temp=True
                break
    if temp:
        print("error")
        continue
    if reverse:
        x.reverse()
        print("[", end="")
        print(",".join(map(str, list(x))), end="")
        print("]")
    else:
        print("[", end="")
        print(",".join(map(str, list(x))), end="")
        print("]")