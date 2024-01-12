command=list(input())

stack=[]

for x in command:
    if x=='+' or x=='-':
        while len(stack)!=0 and stack[-1]!='(':
            print(stack.pop(),end="")
        stack.append(x)
    elif x=='*'or x=='/':
        while len(stack)!=0 and (stack[-1]=='*'or stack[-1]=='/'):
            print(stack.pop(),end="")
        stack.append(x)
    elif x=='(':
        stack.append(x)
    elif x==')':
        while len(stack)!=0 and stack[-1]!='(':
            print(stack.pop(),end="")
        stack.pop()
    else:
        print(x,end="")

while len(stack)!=0:
    print(stack.pop(),end="")
