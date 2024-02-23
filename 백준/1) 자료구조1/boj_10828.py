import sys

n=int(sys.stdin.readline())
stack=[]

for i in range(n):
    order=list(sys.stdin.readline().split())
    if order[0]=="push":
        stack.append(int(order[1]))
    elif order[0]=="pop":
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif order[0]=="size":
        print(len(stack))
    elif order[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif order[0]=="top":
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
