num=[]
for i in range(31):
    num.append(0)

for j in range(28):
    a=int(input())
    num[a]=1

for k in range(1,31):
    if num[k]==0 :
        print(k,end=" ")