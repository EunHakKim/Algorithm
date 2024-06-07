import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input().strip())
    sum=0
    for i in range(N):
        sum+=int(input().strip())

    if sum==0:
        print(0)
    elif sum>0:
        print("+")
    else:
        print("-")