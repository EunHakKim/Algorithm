words=list(input())
temp=0
stack=""

for x in words:
    if x=="<":
        if len(stack)!=0:
            print(stack[::-1],end="")
            stack=""
        temp=1
        print(x,end="")
    elif x==">":
        temp=0
        print(x,end="")
    elif temp==1:
        print(x,end="")
    elif x==" ":
        if len(stack)!=0:
            print(stack[::-1],end="")
            stack=""
        print(x,end="")
    else:
        stack+=x

if len(stack)!=0:
    print(stack[::-1],end="")
    