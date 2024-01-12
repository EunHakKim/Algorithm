n=int(input())

command=list(input())
var=[]
stack=[]

for i in range(n):
    var.append(int(input()))

for x in command:
    if x=='+':
        stack.append(stack.pop()+stack.pop())
    elif x=='-':
        stack.append(-stack.pop()+stack.pop())
    elif x=='*':
        stack.append(stack.pop()*stack.pop())
    elif x=="/":
        stack.append(1/stack.pop()*stack.pop())
    else:
        stack.append(var[ord(x)-65])

print(f"{stack.pop():.2f}")