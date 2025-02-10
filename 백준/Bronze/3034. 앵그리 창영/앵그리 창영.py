import sys
input = sys.stdin.readline

n, w, h = map(int, input().split())
diagonal = (w ** 2 + h ** 2) ** 0.5
for _ in range(n):
    temp = int(input())
    if temp <= diagonal:
        print("DA")
    else:
        print("NE")