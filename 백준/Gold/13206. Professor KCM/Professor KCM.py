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
    result = {}

    for i in range(2, 1001):
        if number[i]:
            prime.append(i)
            result[i] = 0
            j = 2
            for j in range(2 * i, 1001, i):
                number[j] = False

    # 최대값 계산
    for i in nums:
        while i != 1:
            for j in prime:
                cnt = 0
                while i % j == 0:
                    i //= j
                    cnt += 1
                result[j] = max(result[j], cnt)

    for k, v in result.items():
        ans *= (k ** v)
        ans %= 1000000007

    print(ans)