n=int(input())

for i in range(n):
    word=input()
    for j in range(len(word)//2):
        if "()" in word:
            word=word.replace("()","")
    if len(word)==0:
        print("YES")
    else:
        print("NO")