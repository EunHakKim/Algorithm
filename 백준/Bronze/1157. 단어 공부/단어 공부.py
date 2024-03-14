a=input().lower()
b=list(set(a))

cnt=[]

for i in b:
    c=a.count(i)
    cnt.append(c)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(b[cnt.index(max(cnt))].upper())