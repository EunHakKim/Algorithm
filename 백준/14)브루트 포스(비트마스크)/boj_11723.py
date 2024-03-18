import sys

M=int(sys.stdin.readline())
S=[]
for _ in range(M):
    words=list(sys.stdin.readline().split())
    if len(words)==2:
        command=words[0]
        x=int(words[1])
    else:
        command=words[0]
        
    if command=='add':
        if x not in S:
            S.append(x)
    elif command=="remove":
        if x in S:
            S.remove(x)
    elif command=="check":
        if x in S:
            print(1)
        else:
            print(0)
    elif command=="toggle":
        if x in S:
            S.remove(x)
        else:
            S.append(x)
    elif command=="all":
        S.clear()
        for i in range(1,21):
            S.append(i)
    elif command=="empty":
        S.clear()
