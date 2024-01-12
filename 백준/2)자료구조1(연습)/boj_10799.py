word=input()
stack=[]

if "()" in word:
    word=word.replace("()","L")

result=word.count("(")

for x in word:
    if x=="(":
        stack.append("(")
    elif x==")":
        stack.pop()
    elif x=="L":
        result+=len(stack)

print(result)