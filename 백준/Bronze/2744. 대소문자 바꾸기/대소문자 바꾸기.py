word = list(input().strip())
for x in word:
    if x.islower():
        print(x.upper(), end='')
    else:
        print(x.lower(), end='')