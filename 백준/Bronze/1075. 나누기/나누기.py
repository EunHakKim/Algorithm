import sys
input = sys.stdin.readline

n = int(input())
f = int(input())
n = (n // 100) * 100
i = 0

while (n + i) % f != 0:
    i += 1

print(format(i, '02'))