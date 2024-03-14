a=[]
x=0
y=0

for i in range(9):
    num=list(map(int,input().split()))
    for j in num:
        a.append(j)

print(max(a))
print(a.index(max(a))//9+1, a.index(max(a))%9+1)    