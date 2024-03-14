n=int(input())
min=5001

for i in range(n//5+1):
    for j in range(n//3+1):
        if 5*i+3*j==n and i+j<min:
            min=i+j

if(min==5001):
    print(-1)
else:
    print(min)