import sys
n=int(input())

for i in range(n) :
    x, y = sys.stdin.readline().split()
    print(f"Case #{i+1}:", end=" ")
    print(int(x)+int(y))