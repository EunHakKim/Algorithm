E,S,M=map(int,input().split())
count=1

while(True):
    if E==1 and S==1 and M==1:
        break

    if E==1:
        E=15
    else:
        E-=1

    if S==1:
        S=28
    else:
        S-=1

    if M==1:
        M=19
    else:
        M-=1
    
    count+=1

print(count)