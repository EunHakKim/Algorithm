import sys
n=int(input())

for i in range(n) :
    x, y = sys.stdin.readline().split()
    print(int(x)+int(y))