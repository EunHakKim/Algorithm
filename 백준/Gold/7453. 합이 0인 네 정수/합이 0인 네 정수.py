import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
AB, CD = [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A:
    for b in B:
        AB.append(a + b)

for c in C:
    for d in D:
        CD.append(c + d)

AB.sort()
CD.sort()
abpointer, cdpointer = 0, len(CD) - 1
abcd = 0
ans = 0

while abpointer < len(AB) and cdpointer >= 0:
    abcd = AB[abpointer] + CD[cdpointer]
    if abcd > 0:
        cdpointer -= 1
    elif abcd < 0:
        abpointer += 1
    else:
        ab, cd = abpointer + 1, cdpointer - 1

        while ab < len(AB) and AB[abpointer] == AB[ab]: 
            ab += 1
            
        while cd >= 0 and CD[cdpointer] == CD[cd]: 
            cd -= 1
        ans += (ab - abpointer) * (cdpointer - cd) 
        abpointer, cdpointer = ab, cd


print(ans)