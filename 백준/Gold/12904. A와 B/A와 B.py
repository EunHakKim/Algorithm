import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

S=list(input().strip())
T=list(input().strip())

while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
    if S==T:
        print(1)
        exit()

print(0)