import sys

T=int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int,sys.stdin.readline().split())
    if M>=N: 
        temp=0   
        X, Y = y, y
        year=y
        for i in range(M+1):
            if X==x:
                temp=1
                break
            if X+N>M:
                X=X+N-M
            else:
                X+=N
            year+=N
    else:
        temp=0
        X,Y=x,x
        year=x
        for i in range(N+1):
            if Y==y:
                temp=1
                break
            if Y+M>N:
                Y=Y+M-N
            else:
                Y+=M
            year+=M

    if temp==0:
        print(-1)
    else:
        print(year)