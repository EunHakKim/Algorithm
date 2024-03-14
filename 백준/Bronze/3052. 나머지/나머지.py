num=[int(input()) for _ in range(10)]

a=1
b=[num[0]%42]

for i in range(1,10):
    if num[i]%42 not in b :
        b.append(num[i]%42)
        a+=1

print(a)