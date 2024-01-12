s=input()

result=[0]*26

for x in s:
    result[ord(x)-97]+=1

print(*result)