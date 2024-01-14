words=input()

for x in words:
    if x.isalpha():
        if 0<=ord(x)-97<13:
            print(chr(ord(x)+13),end="")
        elif 13<=ord(x)-97<26:
            print(chr(ord(x)-13),end="")
        elif 0<=ord(x)-65<13:
            print(chr(ord(x)+13),end="")
        elif 13<=ord(x)-65<26:
            print(chr(ord(x)-13),end="")
    else:
        print(x,end="")
        