A,B=map(int,input().split())

G=1

for i in range(1,min(A,B)+1):
    if A%i==0 and B%i==0:
        G=i

print(G)
print(int(A*B/G))