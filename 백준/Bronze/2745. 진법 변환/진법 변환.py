num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum=0

n,b=input().split()

n=n[::-1]

for i in range(len(n)):
    sum+=num.index(n[i])*(int(b)**i)

print(sum)
