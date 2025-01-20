import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(set(map(int, input().split())))
    ans = 1

    # 소수 계산
    number = [True for _ in range(1001)]
    number[0], number[1] = False, False
    prime = []

    for i in range(2, 1001):
        if number[i]:
            prime.append(i)
            j = 2
            for j in range(2 * i, 1001, i):
                number[j] = False

    # 최대값 계산
    for i in prime:
        max_temp = 0
        for j in nums:
            temp = 0
            while j % i == 0 and j > 1:
                j //= i
                temp += 1
            max_temp = max(max_temp, temp)
        ans = (ans * (i ** max_temp)) % 1000000007

    print(ans)