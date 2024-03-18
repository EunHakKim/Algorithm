import sys
n=int(input())

for i in range(n) :
    x, y = sys.stdin.readline().split()
    print(f"Case #{i+1}: {int(x)} + {int(y)} =", end=" ")
    print(int(x)+int(y))