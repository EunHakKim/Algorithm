import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    n, m = map(int,input().split())
    arr = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        max_v = max(arr)
        temp = arr.popleft()
        if temp >= max_v:
            if m==0:
                print(cnt)
                break
            else:
                cnt += 1
                n -= 1
                m -= 1
        else:
            arr.append(temp)
            m = (m - 1 + n) % n
        

