n=input()

result=[-1]*26

for x in reversed(n):
    result[ord(x)-97]=n.index(x)

print(*result)