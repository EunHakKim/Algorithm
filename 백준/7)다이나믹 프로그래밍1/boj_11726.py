n=int(input())

count=[0,1,2]

for i in range(3,n+1):
    count.append((count[i-2]+count[i-1])%10007)

print(count[n])