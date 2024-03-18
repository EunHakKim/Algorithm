n=int(input())
m=int(input())

sum=0

for i in range(n):
    sum+=m%10
    m=m//10

print(sum)