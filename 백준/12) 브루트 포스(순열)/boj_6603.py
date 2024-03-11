import itertools

while(True):
    S=list(map(int,input().split()))
    if S[0]==0:
        exit()
    k=S[0]
    S.remove(S[0])
    per=itertools.combinations(S, 6)
    for x in per:
        print(*x)
    print()